#---------------------------IMPORT LIBRARIES---------------------------
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from statistics import mode
import json
#from sklearn.linear_model import LinearRegression

#---------------------------DATA EXTRACTION---------------------------
#from scipy.ndimage import label
from fontTools.varLib import MasterFinder

path1 = 'Dataset/00_sources/ADMISSIONS.csv'
    #Every unique hospitalization for each patient in the database (defines HADM_ID)
    #Cada hospitalización única para cada paciente en la base de datos (define HADM_ID).
path2 = 'Dataset/00_sources/CALLOUT.csv'
    #Information regarding when a patient was cleared for ICU discharge and when the patient was actually discharged.
    #Información sobre cuándo se autorizó el alta de la UCI a un paciente y cuándo se le dio de alta realmente.
path3 = 'Dataset/00_sources/CAREGIVERS.csv'
    #Every caregiver who has recorded data in the database (defines CGID).
    #Todo_cuidador que tenga datos registrados en la base de datos (define CGID).
path4 = 'Dataset/00_sources/CHARTEVENTS.csv'
    #All charted observations for patients.
    #Todas las observaciones registradas para los pacientes.
path5 = 'Dataset/00_sources/CPTEVENTS.csv'
    #Procedures recorded as Current Procedural Terminology (CPT) codes.
    #Procedimientos registrados como códigos de Terminología Procesal Actual (CPT).
path6 = 'Dataset/00_sources/D_CPT.csv'
    #High level dictionary of Current Procedural Terminology (CPT) codes.
    #Diccionario de alto nivel de códigos de terminología procesal actual (CPT).
path7 = 'Dataset/00_sources/D_ICD_DIAGNOSES.csv'
    #Dictionary of International Statistical Classification of Diseases and Related Health Problems (ICD-9) codes relating to diagnoses.
    #Diccionario de códigos de la Clasificación Estadística Internacional de Enfermedades y Problemas de Salud Relacionados (CIE-9) relacionados con los procedimientos.
path8 = 'Dataset/00_sources/D_ICD_PROCEDURES.csv'
    #Dictionary of International Statistical Classification of Diseases and Related Health Problems (ICD-9) codes relating to procedures.
    #Diccionario de códigos de la Clasificación Estadística Internacional de Enfermedades y Problemas de Salud Relacionados (CIE-9) relacionados con los procedimientos.
path9 = 'Dataset/00_sources/D_ITEMS.csv'
    #Dictionary of local codes (’ITEMIDs’) appearing in the MIMIC database, except those that relate to laboratory tests.
    #Diccionario de códigos locales ('ITEMIDs') que aparecen en la base de datos MIMIC, excepto aquellos relacionados con pruebas de laboratorio.
path10 = 'Dataset/00_sources/D_LABITEMS.csv'
    #Dictionary of local codes (’ITEMIDs’) appearing in the MIMIC database that relate to laboratory tests.
    #Diccionario de códigos locales ('ITEMIDs') que aparecen en la base de datos MIMIC que se relacionan con pruebas de laboratorio.
path11 = 'Dataset/00_sources/DATETIMEEVENTS.csv'
    #All recorded observations which are dates, for example time of dialysis or insertion of lines.
    #Todas las observaciones registradas que son fechas, por ejemplo, hora de diálisis o inserción de líneas.
path12 = 'Dataset/00_sources/DIAGNOSES_ICD.csv'
    #Hospital assigned diagnoses, coded using the International Statistical Classification of Diseases and Related Health Problems (ICD) system
    #Diagnósticos asignados por el hospital, codificados según el sistema de Clasificación Estadística Internacional de Enfermedades y Problemas Relacionados con la Salud (CIE).
path13 = 'Dataset/00_sources/DRGCODES.csv'
    #Diagnosis Related Groups (DRG), which are used by the hospital for billing purposes.
    #Grupos relacionados con el diagnóstico (DRG), que utiliza el hospital para fines de facturación.
path14 = 'Dataset/00_sources/ICUSTAYS.csv'
    #Every unique ICU stay in the database (defines ICUSTAY_ID).
    #Cada estancia en UCI única en la base de datos (define ICUSTAY_ID).
path15 = 'Dataset/00_sources/INPUTEVENTS_CV.csv'
    #Intake for patients monitored using the Philips CareVue system while in the ICU, e.g., intravenous medications, enteral feeding, etc.
    #Admisión para pacientes monitorizados mediante el sistema Philips CareVue mientras están en la UCI, por ejemplo, medicamentos intravenosos, alimentación enteral, etc.
path16 = 'Dataset/00_sources/INPUTEVENTS_MV.csv'
    #Intake for patients monitored using the iMDSoft MetaVision system while in the ICU, e.g., intravenous medications, enteral feeding, etc.
    #Admisión de MV para pacientes monitoreados usando el sistema iMDSoft MetaVision mientras están en la UCI, p. ej., medicamentos intravenosos, alimentación enteral, etc.
path17 = 'Dataset/00_sources/LABEVENTS.csv'
    #Laboratory measurements for patients both within the hospital and in outpatient clinics.
    #Mediciones de laboratorio para pacientes tanto dentro del hospital como en consultas externas.
path18 = 'Dataset/00_sources/MICROBIOLOGYEVENTS.csv'
    #Microbiology culture results and antibiotic sensitivities from the hospital database.
    #Resultados de cultivos de microbiología y sensibilidades a antibióticos de la base de datos del hospital.
path19 = 'Dataset/00_sources/NOTEEVENTS.csv'
    #Deidentified notes, including nursing and physician notes, ECG reports, radiology reports, and discharge summaries.
    #Notas no identificadas, incluidas notas de médicos y enfermeras, informes de ECG, informes de radiología y resúmenes de alta.
path20 = 'Dataset/00_sources/OUTPUTEVENTS.csv'
    #Output information for patients while in the ICU.
    #Información de salida para pacientes mientras están en la UCI.
path21 = 'Dataset/00_sources/PATIENTS.csv'
    #Every unique patient in the database (defines SUBJECT_ID).
    #Cada paciente único en la base de datos (define SUBJECT_ID).
path22 = 'Dataset/00_sources/PRESCRIPTIONS.csv'
    #Medications ordered for a given patient.
    #Medicamentos ordenados para un paciente dado.
path23 = 'Dataset/00_sources/PROCEDUREEVENTS_MV.csv'
    #Patient procedures for the subset of patients who were monitored in the ICU using the iMDSoft MetaVision system.
    #Procedimientos de pacientes para el subconjunto de pacientes que fueron monitoreados en la UCI usando el sistema iMDSoft MetaVision.
path24 = 'Dataset/00_sources/PROCEDURES_ICD.csv'
    #Patient procedures, coded using the International Statistical Classification of Diseases and Related Health Problems (ICD) system.
    #Procedimientos de pacientes, codificados utilizando el sistema de Clasificación Estadística Internacional de Enfermedades y Problemas de Salud Relacionados (ICD).
path25 = 'Dataset/00_sources/SERVICES.csv'
    #The clinical service under which a patient is registered.
    #El servicio clínico bajo el cual está registrado un paciente.
path26 = 'Dataset/00_sources/TRANSFERS.csv'
    #Patient movement from bed to bed within the hospital, including ICU admission and discharge.
    #Movimiento de pacientes de cama a cama dentro del hospital, incluyendo ingreso y alta en UCI.

admissions = pd.read_csv(path1)
d_labtimes = pd.read_csv(path10)
datetimeevents = pd.read_csv(path11)
diagnoses_icd = pd.read_csv(path12)
drgcodes = pd.read_csv(path13)
icustays = pd.read_csv(path14)
inputevents_cv = pd.read_csv(path15,low_memory=False)
inputevents_mv = pd.read_csv(path16)
labevents = pd.read_csv(path17)
microbiologyevents = pd.read_csv(path18)
noteevents = pd.read_csv(path19)
callout = pd.read_csv(path2)
outputevents = pd.read_csv(path20)
patients = pd.read_csv(path21)
prescriptions = pd.read_csv(path22)
procedureevents_mv = pd.read_csv(path23)
procedures_icd = pd.read_csv(path24)
services = pd.read_csv(path25)
transfers = pd.read_csv(path26)
caregivers = pd.read_csv(path3)
chartevents = pd.read_csv(path4, low_memory=False)
cptevents = pd.read_csv(path5)
d_cpt = pd.read_csv(path6)
d_icd_diagnoses = pd.read_csv(path7)
d_icd_procedures = pd.read_csv(path8)
d_items = pd.read_csv(path9)

#------------------------------FIRST STEP------------------------------

#patients_admissions = pd.merge(admissions, patients, on = 'subject_id')
#patients_admissions_icustays = pd.merge(patients_admissions, icustays, left_on = 'hadm_id', right_on = 'subject_id')

#print(patients_admissions_icustays[['subject_id_x','subject_id_y']].head())

#                        Repeat ehr-exploration
#                          github repository

#--------------------------DATA PER PATIENT--------------------------
sepsis_variants = ['SEPSIS', 'SEPSIS_TELEMETRY', 'SEPSIS_PNEUMONIA_TELEMETRY', 'UROSEPSIS', 'SEPSIS_UTI', 'SEPSIS_ UTI']

patients_sepsis = admissions[admissions.diagnosis.isin(sepsis_variants)]
patients_sepsis_id = patients_sepsis['subject_id'].unique()
#[40601, 41976, 10006, 10013, 10036, 10056, 10088, 10094]

#----------------DATA OF SEPSIS PATIENT IN EACH TABLE---------------


callout_sepsis = callout[callout.subject_id.isin(patients_sepsis_id)]
cptevents_sepsis = cptevents[cptevents.subject_id.isin(patients_sepsis_id)]
datetimeevents_sepsis = datetimeevents[datetimeevents.subject_id.isin(patients_sepsis_id)]
diagnoses_icd_sepsis = diagnoses_icd[diagnoses_icd.subject_id.isin(patients_sepsis_id)]
drgcodes_sepsis = drgcodes[drgcodes.subject_id.isin(patients_sepsis_id)]
icustays_sepsis = icustays[icustays.subject_id.isin(patients_sepsis_id)]
inputevents_mv_sepsis = inputevents_mv[inputevents_mv.subject_id.isin(patients_sepsis_id)]
inputevents_cv_sepsis = inputevents_cv[inputevents_cv.subject_id.isin(patients_sepsis_id)]
labevents_sepsis = labevents[labevents.subject_id.isin(patients_sepsis_id)]
microbiologyevents_sepsis = microbiologyevents[microbiologyevents.subject_id.isin(patients_sepsis_id)]
outputevents_sepsis = outputevents[outputevents.subject_id.isin(patients_sepsis_id)]
prescriptions_sepsis = prescriptions[prescriptions.subject_id.isin(patients_sepsis_id)]
procedureevents_mv_sepsis = procedureevents_mv[procedureevents_mv.subject_id.isin(patients_sepsis_id)]
procedures_icd_sepsis = procedures_icd[procedures_icd.subject_id.isin(patients_sepsis_id)]
services_sepsis = services[services.subject_id.isin(patients_sepsis_id)]
transfers_sepsis = transfers[transfers.subject_id.isin(patients_sepsis_id)]
chartevents_sepsis = chartevents[chartevents.subject_id.isin(patients_sepsis_id)]

#---------------------------------------------------------------------------------------

#---------------------Ubicaciones de los pacientes, DIAGRAMA ---------------------------

sepsis_id = list(transfers_sepsis.subject_id.unique())
transfers_sepsis[['intime_date', 'intime_hour']] = transfers_sepsis.intime.str.split(' ',expand = True)
transfers_sepsis[['outtime_date', 'outtime_hour']] = transfers_sepsis.outtime.str.split(' ',expand = True)
transfers_sepsis[['intime_hour1', 'intime_min', 'intime_seg']] = \
       transfers_sepsis.intime_hour.str.split(':',expand = True)
transfers_sepsis = transfers_sepsis.reindex(columns = ['row_id', 'subject_id', 'hadm_id', 'icustay_id', 'dbsource',
       'eventtype', 'prev_careunit', 'curr_careunit', 'prev_wardid', 'curr_wardid', 'intime', 'intime_date',
       'intime_hour', 'intime_hour1', 'intime_min', 'intime_seg', 'outtime', 'outtime_date', 'outtime_hour', 'los'])
transfers_sepsis = transfers_sepsis.drop(['outtime', 'intime'], axis = 1)

#DIAGRAMAS SEPARADOS PARA CADA PACIENTE
for a in range(0, len(sepsis_id)):
       fig, ax = plt.subplots()
       transfers_sepsis0 = transfers_sepsis[transfers_sepsis.subject_id == sepsis_id[a]]
       transfers_sepsis1 = transfers_sepsis0[transfers_sepsis0['eventtype'] == 'transfer']
       transfers_admit = transfers_sepsis0[transfers_sepsis0['eventtype'] == 'admit']
       transfers_dis = transfers_sepsis0[transfers_sepsis0['eventtype'] == 'discharge']
       transfers_admit_ICU = transfers_sepsis0[pd.isna(transfers_sepsis0['curr_careunit']) == False]
       transfers_dis_ICU = transfers_sepsis0[pd.isna(transfers_sepsis0['prev_careunit']) == False]
       ax.scatter(x=list(transfers_sepsis0['intime_date']), y=pd.to_numeric(transfers_sepsis0['intime_hour1'],
              errors='coerce'), color = 'w')
       for j in range(0, len(list(transfers_admit_ICU['intime_hour1']))):
           horas = [pd.to_numeric(list(transfers_admit_ICU['intime_hour1'])[j]), pd.to_numeric(list(transfers_dis_ICU['intime_hour1'])[j])]
           fecha = [list(transfers_admit_ICU['intime_date'])[j], list(transfers_dis_ICU['intime_date'])[j]]
           ax.plot(fecha, horas, color='tab:purple')
       ax.plot(fecha, horas, color='tab:purple', label='Time in ICU')
       ax.grid(color='lightgray', linestyle='dashed')
       ax.scatter(x=list(transfers_sepsis1['intime_date']), y=pd.to_numeric(transfers_sepsis1['intime_hour1'],
              errors='coerce'), label='transfers', marker='^')
       ax.scatter(x=list(transfers_admit['intime_date']), y=pd.to_numeric(transfers_admit['intime_hour1'],
              errors='coerce'), label='admit')
       ax.scatter(x=list(transfers_dis['intime_date']), y=pd.to_numeric(transfers_dis['intime_hour1'],
              errors='coerce'), label='discharge', marker='_')
       #ax.scatter(x=list(transfers_admit_ICU['intime_date']), y=pd.to_numeric(transfers_admit_ICU['intime_hour1'],
       #       errors='coerce'), label='admit in ICU', marker='>')
       #ax.scatter(x=list(transfers_dis_ICU['intime_date']), y=pd.to_numeric(transfers_dis_ICU['intime_hour1'],
       #       errors='coerce'), label='discharge of ICU', marker='H')

       x01 = sepsis_id[a]
       x02 = mode(admissions[admissions['subject_id'] == sepsis_id[a]]['diagnosis'])
       ax.set_title('Paciente {0}: {1}'.format(x01,x02))
       fig.autofmt_xdate(rotation=60)
       ax.set_ylabel("Hour")
       ax.set_xlabel("Date:(Day/Month)")
       ax.legend(loc='upper right')
#plt.show()

#---------------------------------------------------------------------------------------

chartevents_sepsis[['charttime_date', 'charttime_hour']] = chartevents_sepsis.charttime.str.split(' ',expand = True)
chartevents_sepsis[['storetime_date', 'storetime_hour']] = chartevents_sepsis.storetime.str.split(' ',expand = True)
chartevents_sepsis = chartevents_sepsis.reindex(columns = ['row_id', 'subject_id', 'hadm_id', 'icustay_id', 'itemid',
       'charttime', 'charttime_date', 'charttime_hour', 'storetime_date', 'storetime_hour', 'storetime',
       'cgid', 'value', 'valuenum', 'valueuom', 'warning', 'error', 'resultstatus', 'stopped'])
chartevents_sepsis = chartevents_sepsis.drop(['charttime', 'storetime'], axis = 1)

#----------------------------------JSONs------------------------------------
#DICTIONARIES
inputevents_cv_sepsis_dir = d_items.merge(inputevents_cv_sepsis, on='itemid', how='right')
inputevents_mv_sepsis_dir = d_items.merge(inputevents_mv_sepsis, on='itemid', how='right')
labevents_sepsis_dir = d_labtimes.merge(labevents_sepsis, on='itemid', how='right')
chartevents_sepsis_dir = d_items.merge(chartevents_sepsis, on='itemid', how='right')

#---MASTER JSON---MASTER JSON---MASTER JSON---MASTER JSON---MASTER JSON---MASTER JSON---MASTER JSON---MASTER JSON---MAST
JSON = {}
JSON["Static_clinical_variables"] = []
for i in range(0, len(list(sepsis_id))):
    #PATIENT ID
    json_id = list(patients_sepsis_id)[i]

    #DEMOGRAFIC
    json_dob = str(patients[patients['subject_id'] == patients_sepsis_id[i]]['dob'].item())
    json_dod = str(patients[patients['subject_id'] == patients_sepsis_id[i]]['dod'].item())
    json_sex = str(list(patients[patients['subject_id'] == patients_sepsis_id[i]]['gender'])[0])
    json_rlgn = str(list(admissions[admissions['subject_id'] == sepsis_id[i]]['religion'])[0])
    json_ms = str(list(admissions[admissions['subject_id'] == sepsis_id[i]]['marital_status'])[0])
    json_et = str(list(admissions[admissions['subject_id'] == sepsis_id[i]]['ethnicity'])[0])

    #ADMISSIONS
    json_idh = list(transfers_sepsis[transfers_sepsis['subject_id'] ==
        list(patients_sepsis_id)[i]][transfers_sepsis[transfers_sepsis['subject_id'] ==
        list(patients_sepsis_id)[i]]['eventtype'] == 'admit']['intime_date'])
    json_fdh = list(transfers_sepsis[transfers_sepsis['subject_id'] ==
        list(patients_sepsis_id)[i]][transfers_sepsis[transfers_sepsis['subject_id'] ==
        list(patients_sepsis_id)[i]]['eventtype'] == 'discharge']['intime_date'])
    json_dia = list(admissions[admissions['subject_id'] == sepsis_id[i]]['diagnosis'])

    JSON_att = {}
    JSON_att["Admissions"] = []

    for l in range(0, len(json_idh)):
        JSON_att["Admissions"].append(dict(
                initial_date_hospitalization = json_idh[l],
                final_date_hospitalization = json_fdh[l],
                diagnosis_of_admission = json_dia[l]
        ))

    JSON["Static_clinical_variables"].append(dict(
        Head= {
            "id_patient": json_id.item()
        },
        Body={
            "demographic":{
                "date_of_birth": json_dob,
                "date_of_death": json_dod,
                "sex": json_sex,
                "religion": json_rlgn,
                "marital_status": json_ms,
                "ethnicity": json_et
                },
            "atention": JSON_att,
        }
    ))

with open('Dataset/01_preprocessing/Master_JSON.json', 'w') as file:
    json.dump(JSON, file, indent=4)
#-----------------------------------------------------------------------------------------------------------------------


#---INTERNAL SPECIFIC JSON---INTERNAL SPECIFIC JSON---INTERNAL SPECIFIC JSON---INTERNAL SPECIFIC JSON---INTERNAL SPECIFI
JSON = {}
JSON["Static_clinical_variables"] = []
for j in range(0, len(sepsis_id)):
    patient = patients[patients['subject_id'] == patients_sepsis_id[j]]
    # DEMOGRAFIC
    json_dob = str(patient['dob'].item())
    json_dod = str(patient['dod'].item())
    json_sex = list(patient['gender'])[0]

    JSON["Static_clinical_variables"].append(dict(
        Id = {
            "id_patient": list(patients_sepsis_id)[j].item()
        },
        Demographic= {
            "date of birth": json_dob,
            "date of death": json_dod,
            "sex": json_sex
        }
    ))

    for i in list(admissions[admissions['subject_id'] == sepsis_id[j]]['hadm_id']):

        #ADMISSION
        json_idh = str(transfers_sepsis[transfers_sepsis['subject_id'] ==
            list(patients_sepsis_id)[j]][transfers_sepsis[transfers_sepsis['subject_id'] ==
            list(patients_sepsis_id)[j]]['eventtype'] == 'admit'][transfers_sepsis[transfers_sepsis['subject_id'] ==
            list(patients_sepsis_id)[j]][transfers_sepsis[transfers_sepsis['subject_id'] ==
            list(patients_sepsis_id)[j]]['eventtype'] == 'admit'].hadm_id == i]['intime_date'].item())
        json_fdh = str(transfers_sepsis[transfers_sepsis['subject_id'] ==
            list(patients_sepsis_id)[j]][transfers_sepsis[transfers_sepsis['subject_id'] ==
            list(patients_sepsis_id)[j]]['eventtype'] == 'discharge'][transfers_sepsis[transfers_sepsis['subject_id'] ==
            list(patients_sepsis_id)[j]][transfers_sepsis[transfers_sepsis['subject_id'] ==
            list(patients_sepsis_id)[j]]['eventtype'] == 'discharge'].hadm_id == i]['intime_date'].item())
        json_dia = admissions[admissions['subject_id'] ==
            sepsis_id[j]][admissions[admissions['subject_id'] == sepsis_id[j]].hadm_id == i].diagnosis.item()

        #ATTENTION
        med_cv = inputevents_cv_sepsis_dir[inputevents_cv_sepsis_dir['subject_id'] ==
                list(patients_sepsis_id)[j]].reset_index()[['charttime','label','amount','amountuom']]
        med_mv = inputevents_mv_sepsis_dir[inputevents_mv_sepsis_dir['subject_id'] ==
                list(patients_sepsis_id)[j]].reset_index()[['starttime', 'label', 'amount', 'amountuom']]
        med_mv = med_mv.rename(columns={'starttime':'charttime'})

        if (med_cv.empty):
            json_med = med_mv
        else:
            json_med = med_cv

        JSON_mtc = {}
        JSON_mtc["Medication"] = []

        for m in range(0, len(json_med)):
            JSON_mtc["Medication"].append(dict(
                charttime= list(json_med.charttime)[m],
                label= list(json_med.label)[m],
                amount= list(json_med.amount)[m],
                amountuom= list(json_med.amountuom)[m]
            ))

        #---IMPORTANTE---IMPORTANTE---IMPORTANTE---IMPORTANTE---IMPORTANTE---IMPORTANTE---IMPORTANTE---
        #
        #      PARTIENDO DE LA IDEA DE QUE LOS ID FALTANTES DE HADM_ID SEAN POR MOTIVOS
        #      DE FORMATO Y QUE TODOS LOS EVENTOS QUE ALLÍ SE ENCUENTRAN SON DE HOSPITALIZACIÓN
        #
        #---IMPORTANTE---IMPORTANTE---IMPORTANTE---IMPORTANTE---IMPORTANTE---IMPORTANTE---IMPORTANTE---

        lab_adm = labevents_sepsis_dir[labevents_sepsis_dir['hadm_id'] ==
            list(patients_sepsis_id)[j]].reset_index()[['charttime', 'label', 'value', 'valueuom','flag']]
        lab_sub = labevents_sepsis_dir[labevents_sepsis_dir['subject_id'] ==
            list(patients_sepsis_id)[j]].reset_index()[['charttime','label','value','valueuom','flag']]

        if(lab_adm.empty):
            json_lab = lab_sub
        else:
            json_lab = lab_adm

        JSON_labs = {}
        JSON_labs["Lab_Test"] = []

        for n in range(0, len(json_lab)):
            JSON_labs["Lab_Test"].append(dict(
                charttime = list(json_lab.charttime)[n],
                label = list(json_lab.label)[n],
                value = list(json_lab.value)[n],
                valueuom = list(json_lab.valueuom)[n],
                flag = list(json_lab.flag)[n]
            ))

        json_mcb = microbiologyevents_sepsis[microbiologyevents_sepsis.hadm_id ==
            i][['charttime','spec_type_desc','org_name','ab_name']]

        JSON_mblgy = {}
        JSON_mblgy["Microbiology_Test"] = []
        for t in range(0, len(json_mcb)):
            JSON_mblgy["Microbiology_Test"].append(dict(
                charttime = list(json_mcb.charttime)[t],
                spec_type_desc = list(json_mcb.spec_type_desc)[t],
                org_name = list(json_mcb.org_name)[t],
                ab_name = list(json_mcb.ab_name)[t]
            ))

        json_che = chartevents_sepsis_dir[chartevents_sepsis_dir.hadm_id ==
            i][['charttime_date','charttime_hour','label','value','valuenum','valueuom','category']]

        JSON_even = {}
        JSON_even["Events"] =[]
        for b in range(0,len(json_che)):
            JSON_even["Events"].append(dict(
                charttime_date = list(json_che.charttime_date)[b],
                charttime_hour= list(json_che.charttime_hour)[b],
                label= list(json_che.label)[b],
                value= list(json_che.value)[b],
                valuenum= list(json_che.valueuom)[b],
                category= list(json_che.category)[b]
            ))

        JSON["Static_clinical_variables"].append(dict(
            Body = {
                "admission": {
                    # To_do: "rol_patient": ,
                    "identification_of_admissioon": i,
                    "initial_date_hospitalization": json_idh,
                    "final_date_hospitalization": json_fdh,
                    "diagnosis_of_admission": json_dia
                },
                "attention":{
                    "medicine_given_while_state": JSON_mtc,
                    "laboratory_test": JSON_labs,
                    "microbiology_test": JSON_mblgy,
                    "chartevents": JSON_even
                },
                "clinical_notes":{
                    #null
                }
            }
        ))

with open('Dataset/01_preprocessing/Internal_JSON.json', 'w') as file:
    json.dump(JSON, file, indent = 4)
#-----------------------------------------------------------------------------------------------------------------------
