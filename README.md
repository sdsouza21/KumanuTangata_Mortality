# KumanuTangata_Mortality
# Project Abstract
**Objective:** To examine cause-specific and all-cause mortality among former first-class male rugby players and compare mortality rates to those of the general population.  
**Design:** Nationwide retrospective cohort study. 
**Setting:** New Zealand 
**Participants:** A cohort of 12,861 first-class male rugby players active between 1950 and 2000, compared to 2,394,342 males from the general population. General population males were weighted to match players by birth year, overseas-born status, and ethnicity.  
**Main outcome measures:** All-cause mortality and cause-specific mortality (including cancer, cardiovascular, respiratory, metabolic, and neurodegenerative diseases) from mortality records between 1988 to 2020. Premature mortality burden was reported using years of life lost.   
**Results:** By the end of the study period, 3,378 (26.3%) former players and 656,139 (27.4%) general population males had died. Cancer and cardiovascular diseases were the leading causes of death, together accounting for 2,280 (67.5%) of player deaths and 427,419 (65.1%) of general population deaths. Former players had lower all-cause (hazard ratio 0.93, 95% confidence interval 0.90 to 0.96), respiratory (0.59, 0.51 to 0.68) and metabolic (0.68, 0.55 to 0.83) mortality, but higher neurodegenerative disease mortality (1.31, 1.15 to 1.50). Age-stratified analyses showed lower all-cause mortality in players until age 80, after which rates exceeded those of the general population; elevated neurodegenerative disease mortality was only observed after age 80. Mean age at death was 1.7 (1.4 to 1.9) years higher in players, and they experienced 0.7 (0.5 to 0.8) fewer years of premature mortality than general population males, despite a small degree of excess mortality due to neurodegenerative diseases (0.04, 0.02 to 0.06 years).  
**Conclusions:** Mortality patterns among former rugby players were generally similar to the New Zealand
# Statistical analyses
Data management was performed using SAS Enterprise Guide (version 8.3), statistical modelling in Stata (version 16.1), and descriptive statistics in Microsoft Excel 2024. Data visualisations were generated using Python 3.12 with the Pandas, Numpy, and Matplotlib libraries.  

To report the relative frequency of each cause of death, we calculated: 1) the percentage of deaths due to each cause among all deaths in each cohort, and 2) the percentage of each cohort that died from each cause. Risk differences (RD) between cohorts were derived using the percent of each cohort that died and expressed per 1,000 individuals. Cohen’s d was used to quantify differences between the cohorts in age-at-death. 

Premature mortality burden was reported using years of life lost (YLL) per 1000 individuals for each cause of death, calculated according to World Health Organization (WHO) guidelines using a reference ‘healthy life span’ of 89.2 years, derived from WHO life-tables applicable to our cohorts. Differences in YLL per 1000 individuals between cohorts were calculated for each cause of death.  

We used Cox proportional hazards models to analyse differences in death rates by cause. For cause-specific mortality analyses, individuals were tracked from age 30, with right-censoring at emigration or end of follow-up; deaths from causes other than that being analysed were also censored. The proportional hazards assumption was tested using Schoenfeld residuals. To account for time-dependent effects, we conducted stratified analyses by 10-year age bands (30–39, 40–49, 50–59, 60–69, 70–79, 80–89, 90+), with pre- and post-period events censore. Kaplan-Meier survival curves were also produced. To address competing risks, where death from one cause precludes death from another, we performed sensitivity analyses using Fine-Gray subdistribution hazard models.
# Table of contents
1. Mortality of former first-class rugby players_BMJ_codefile.txt
  - SAS and Stata code for data management and all analyses (including supplemental material)
  
2. Mortality paper Figure 1.py
  - Python code for producing Figure 1
    
3. Mortality paper A Figure 2 BMJ compliant.py
  - Python code for producing Figure 2
  
4. Mortality paper A Figure 3 BMJ compliant.py
   - Python code for producing Figure 3
  
# Acknowledgements and authors
**Acknowledgements**
This work was supported by World Rugby Limited and the New Zealand Rugby Foundation [grant number G-2004-00963]. World Rugby obtained an independent, external review of the project plan prior to funding. The study funders had no role in study conception or design; data collection, analysis, and interpretation; and manuscript preparation and submission.  
We thank Statistics New Zealand and their staff for access to the Integrated Data Infrastructure and timely review of outputs. We also acknowledge the Public Policy Institute at the University of Auckland for access to their Statistics New Zealand Datalab, and Clive Akers for his collation of player records in the New Zealand Rugby Register.  

**Manuscript authors**
- Kenneth L. Quarrie, PhD 
- Chao Li, PhD 
- Barry J. Milne, PhD 
- Francesca Anns, BA(Hons) 
- Andrew Gardner, PhD 
- Ian Murphy, MB ChB 
- Evert Verhagen, PhD 
- Craig Wright, BSc 
- Susan M. B. Morton, PhD 
- Thomas Lumley, PhD 
- Lynette Tippett, PhD 
- John W. Orchard, MD, PhD 
- Joshua P. McGeown, PhD 
- Stephanie D’Souza, PhD

**Manuscript authors**
- Kenneth L. Quarrie, PhD 
- Chao Li, PhD 
- Barry J. Milne, PhD
- Stephanie D’Souza, PhD

# Stats NZ Disclaimer
These results are not official statistics. They have been created for research purposes from the Integrated Data Infrastructure (IDI) which is carefully managed by Statistics New Zealand. For more information about the IDI please visit https://www.stats.govt.nz/integrated-data/.  
