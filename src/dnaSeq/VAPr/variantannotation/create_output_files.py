import pandas
import vcf
from pymongo import MongoClient


class FileWriter(object):

    #TODO: Tests for new classes.
    def __init__(self, db_name, collection_name):
        self.collection_name = collection_name
        self.db_name = db_name

    def generate_unfiltered_annotated_csv(self, filepath):
        """
        :param list_dictionaries: list of annotated variants in dictionary
        :param filepath: filpath (including name of output file) to which the output will be written
        :return: annotated csv file
        """
        client = MongoClient()
        db = getattr(client, self.db_name)
        collection = getattr(db, self.collection_name)
        all_my_data = list(collection.find({}))

        df = pandas.DataFrame(all_my_data)

        with open(filepath, "w") as f:
            df.to_csv(f)

        return 'Finished writing annotated CSV file'

    def generate_unfiltered_annotated_vcf(self, vcf_input_path, vcf_output_path):
        """
        :param vcf_input_path: template vcf file (inital vcf from which a new one will be created)
        :param vcf_output_path: name and filepath to where new vcf file will be written
        :return: writed vcf file to specified directory
        """
        client = MongoClient()
        db = getattr(client, self.db_name)
        collection = getattr(db, self.collection_name)
        all_my_data = list(collection.find({}))

        chr_vars = []
        location_vars_ant = []
        location_vars_pos = []

        for i in range(0, len(all_my_data)):
            if all_my_data[i]['Chr'] == 'chrMT':
                chr_vars.append('chrM')
            else:
                chr_vars.append(all_my_data[i]['Chr'].encode('ascii','ignore'))
            location_vars_ant.append(all_my_data[i]['Start'] + 1)
            location_vars_pos.append(all_my_data[i]['Start'] - 1)

        vcf_reader = vcf.Reader(filename=vcf_input_path)
        vcf_writer = vcf.Writer(open(vcf_output_path, 'w'), vcf_reader)

        for i in range(0, len(chr_vars)):
            for record in vcf_reader.fetch(chr_vars[i].encode('ascii','ignore'), location_vars_pos[i], location_vars_ant[i]):
                record.INFO.update(all_my_data[i])
                vcf_writer.write_record(record)

        return 'Finished writing annotated VCF file'

    @staticmethod
    def generate_annotated_csv(list_dictionaries, filepath):
        """
        :param list_dictionaries: list of annotated variants in dictionary
        :param filepath: filpath (including name of output file) to which the output will be written
        :return: annotated csv file
        """
        df = pandas.DataFrame(list_dictionaries)
        with open(filepath, "w") as f:
            df.to_csv(f)

        return 'Finished writing annotated, filtered CSV file'

    @staticmethod
    def generate_annotated_vcf(joint_list, vcf_input_path, vcf_output_path):
        """
        :param vcf_input_path: template vcf file (initial vcf from which a new one will be created)
        :param vcf_output_path: name and filepath to where new vcf file will be written
        :param joint_list: list of dictionaties contatining annotations from ANNOVAR & myvariant
        :return:
        """
        chr_vars = []
        location_vars_ant = []
        location_vars_pos = []

        for i in range(0, len(joint_list)):
            if joint_list[i]['Chr'] == 'chrMT':
                chr_vars.append('chrM')
            else:
                chr_vars.append(joint_list[i]['Chr'].encode('ascii','ignore'))
            location_vars_ant.append(joint_list[i]['Start'] + 1)
            location_vars_pos.append(joint_list[i]['Start'] - 1)

        vcf_reader = vcf.Reader(filename=vcf_input_path)
        vcf_writer = vcf.Writer(open(vcf_output_path, 'w'), vcf_reader)

        for i in range(0, len(chr_vars)):
            for record in vcf_reader.fetch(chr_vars[i].encode('ascii','ignore'), location_vars_pos[i], location_vars_ant[i]):
                record.INFO.update(joint_list[i])
                vcf_writer.write_record(record)

        return 'Finished writing annotated, filtered VCF file'
