__author__ = 'Guorong Xu<g1xu@ucsd.edu>'

import os

def preproecess():
    workspace = "/shared/workspace/data_archive/SmallRNASeq"
    s3_input_files_address = "s3://ucsd-ccbb-wgs-test-us-east-1/SmallRNA_Sequencing_Pipeline_Code/test_data/050316_Wynnis_Tom_mirseq/160502_K00180_0165_AH7HG5BBXX"
    s3_output_files_address = "s3://ucsd-ccbb-wgs-test-us-east-1/SmallRNA_Sequencing_Pipeline_Code/test_data/050316_Wynnis_Tom_mirseq/fastq"
    sample_list = ["AD10-WK0_TCCCGA_S93_L002_R1_001.fastq.gz", "AD10-WK12_ACAGTG_S52_L002_R1_001.fastq.gz", "AD10-WK16_GTGGCC_S19_L001_R1_001.fastq.gz", "AD10-WK24_ATGAGC_S73_L002_R1_001.fastq.gz", "AD10-WK8_CATTTT_S34_L001_R1_001.fastq.gz", "AD13-WK0_CGTACG_S21_L001_R1_001.fastq.gz", "AD13-WK105_GGTAGC_S23_L001_R1_001.fastq.gz", "AD13-WK12_GGCTAC_S10_L001_R1_001.fastq.gz", "AD13-WK16_ATGTCA_S14_L001_R1_001.fastq.gz", "AD13-WK20_GTTTCG_S68_L002_R1_001.fastq.gz", "AD13-WK24_CACTCA_S79_L002_R1_001.fastq.gz", "AD13-WK28_CTATAC_S38_L001_R1_001.fastq.gz", "AD13-WK32_ATTCCT_S26_L001_R1_001.fastq.gz", "AD13-WK40_CTCAGA_S87_L002_R1_001.fastq.gz", "AD13-WK40_CTTGTA_S11_L001_R1_001.fastq.gz", "AD13-WK52_CAGATC_S54_L002_R1_001.fastq.gz", "AD13-WK8_AGTTCC_S61_L002_R1_001.fastq.gz", "AD15-WK0_TGACCA_S51_L002_R1_001.fastq.gz", "AD15-WK12_ACTTGA_S55_L002_R1_001.fastq.gz", "AD15-WK16_CAGGCG_S32_L001_R1_001.fastq.gz", "AD15-WK24_CAGATC_S7_L001_R1_001.fastq.gz", "AD15-WK4_GTCCGC_S65_L002_R1_001.fastq.gz", "AD15-WK8_CCGTCC_S63_L002_R1_001.fastq.gz", "AD16-WK0_CATGGC_S81_L002_R1_001.fastq.gz", "AD16-WK12_CGGAAT_S36_L001_R1_001.fastq.gz", "AD16-WK20_TTAGGC_S3_L001_R1_001.fastq.gz", "AD16-WK24_CGTACG_S69_L002_R1_001.fastq.gz", "AD16-WK4_GGCTAC_S58_L002_R1_001.fastq.gz", "AD16-WK56_TCATTC_S44_L001_R1_001.fastq.gz", "AD16-WK8_TAGCTT_S9_L001_R1_001.fastq.gz", "AD17-WK0_GTCCGC_S17_L001_R1_001.fastq.gz", "AD17-WK12_TATAAT_S91_L002_R1_001.fastq.gz", "AD17-WK16_CGATGT_S2_L001_R1_001.fastq.gz", "AD17-WK20_TCGGCA_S47_L001_R1_001.fastq.gz", "AD17-WK24_TACAGC_S42_L001_R1_001.fastq.gz", "AD17-WK52_ACTGAT_S72_L002_R1_001.fastq.gz", "AD17-WK73_GTGAAA_S18_L001_R1_001.fastq.gz", "AD17-WK8_AGTTCC_S13_L001_R1_001.fastq.gz", "AD2-WK16_CCAACA_S83_L002_R1_001.fastq.gz", "AD2-WK20_GGTAGC_S71_L002_R1_001.fastq.gz", "AD2-WK4_GTAGAG_S16_L001_R1_001.fastq.gz", "AD2-WK8_CAGGCG_S80_L002_R1_001.fastq.gz", "AD3-WK0_TAATCG_S41_L001_R1_001.fastq.gz", "AD3-WK12_CGGAAT_S84_L002_R1_001.fastq.gz", "AD3-WK16_ATGTCA_S62_L002_R1_001.fastq.gz", "AD3-WK24_CAACTA_S76_L002_R1_001.fastq.gz", "AD3-WK4_ATCACG_S48_L002_R1_001.fastq.gz", "AD3-WK52_GAGTGG_S70_L002_R1_001.fastq.gz", "AD4-WK0_CCGTCC_S15_L001_R1_001.fastq.gz", "AD4-WK12_TCATTC_S92_L002_R1_001.fastq.gz", "AD4-WK16_CGATGT_S49_L002_R1_001.fastq.gz", "AD4-WK24_GTAGAG_S64_L002_R1_001.fastq.gz", "AD4-WK32_TCGGCA_S95_L002_R1_001.fastq.gz", "AD4-WK40_GCCAAT_S6_L001_R1_001.fastq.gz", "AD4-WK4_CCAACA_S35_L001_R1_001.fastq.gz", "AD4-WK52_GACGAC_S88_L002_R1_001.fastq.gz", "AD4-WK61_GCCAAT_S53_L002_R1_001.fastq.gz", "AD4-WK8_ATGAGC_S25_L001_R1_001.fastq.gz", "AD4-WK8_ATTCCT_S74_L002_R1_001.fastq.gz", "AD5-WK0_TACAGC_S90_L002_R1_001.fastq.gz", "AD5-WK12_GTGAAA_S66_L002_R1_001.fastq.gz", "AD5-WK16_TTAGGC_S50_L002_R1_001.fastq.gz", "AD5-WK24_GTGGCC_S67_L002_R1_001.fastq.gz", "AD5-WK4_GAGTGG_S22_L001_R1_001.fastq.gz", "AD5-WK52_GATCAG_S56_L002_R1_001.fastq.gz", "AD6-WK0_AGTCAA_S60_L002_R1_001.fastq.gz", "AD6-WK12_CACTCA_S31_L001_R1_001.fastq.gz", "AD6-WK16_TCCCGA_S45_L001_R1_001.fastq.gz", "AD6-WK20_CTAGCT_S85_L002_R1_001.fastq.gz", "AD6-WK24_CAAAAG_S27_L001_R1_001.fastq.gz", "AD6-WK4_TAGCTT_S57_L002_R1_001.fastq.gz", "AD6-WK52_TAATCG_S89_L002_R1_001.fastq.gz", "AD6-WK8_TCGAAG_S94_L002_R1_001.fastq.gz", "AD7-WK0_CTCAGA_S39_L001_R1_001.fastq.gz", "AD7-WK12_TATAAT_S43_L001_R1_001.fastq.gz", "AD7-WK145_AGTCAA_S12_L001_R1_001.fastq.gz", "AD7-WK20_CTATAC_S86_L002_R1_001.fastq.gz", "AD7-WK4_CACCGG_S77_L002_R1_001.fastq.gz", "AD7-WK52_GATCAG_S8_L001_R1_001.fastq.gz", "AD7-WK8_ACAGTG_S5_L001_R1_001.fastq.gz", "AD8-WK0_CATGGC_S33_L001_R1_001.fastq.gz", "AD8-WK12_CACGAT_S30_L001_R1_001.fastq.gz", "AD8-WK16_CTTGTA_S59_L002_R1_001.fastq.gz", "AD8-WK24_ACTGAT_S24_L001_R1_001.fastq.gz", "AD8-WK36_GTTTCG_S20_L001_R1_001.fastq.gz", "AD8-WK40_CTAGCT_S37_L001_R1_001.fastq.gz", "AD8-WK44_TGACCA_S4_L001_R1_001.fastq.gz", "AD8-WK4_GACGAC_S40_L001_R1_001.fastq.gz", "AD8-WK52_CAAAAG_S75_L002_R1_001.fastq.gz", "AD8-WK88_ATCACG_S1_L001_R1_001.fastq.gz", "AD8-WK88_TCGAAG_S46_L001_R1_001.fastq.gz", "AD9-WK0_CACGAT_S78_L002_R1_001.fastq.gz", "AD9-WK12_CACCGG_S29_L001_R1_001.fastq.gz", "AD9-WK24_CAACTA_S28_L001_R1_001.fastq.gz", "AD9-WK52_CATTTT_S82_L002_R1_001.fastq.gz", "Undetermined_S0_L001_R1_001.fastq.gz", "Undetermined_S0_L002_R1_001.fastq.gz"]

    for sample_name in sample_list:
        sample_name = sample_name[:-9]
        os.popen("qsub " + workspace + "/preprocess.sh " + workspace + " " + sample_name + " " + s3_input_files_address + " " + s3_output_files_address)

if __name__ == "__main__":
    preproecess()