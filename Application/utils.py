import random
import pandas as pd
import csv

from pandas.core.dtypes.missing import isna


def prio_bac(bac, nom_fichier):
    data = pd.read_csv(nom_fichier, sep = ";")
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data.columns = data.columns.str.replace(' ', '') 
    data.columns = data.columns.str.replace('(', '') 
    data.columns = data.columns.str.replace(')', '') 
    dico = {}
    i=0
    if bac == "S":
        for elem in data.NuméroINE :
            if data.Classement[i] == "ECF":
                if data.SérieCode[i] == "S":
                    dico[elem] = 100

                elif data.SérieCode[i] == "ES" or data.SérieCode[i] == "STAV":
                    dico[elem] = 10

                elif data.SérieCode[i] == "ST2S":
                    dico[elem] = 15

                else :
                    dico[elem] = 0
            i+=1

    if bac == "ES":
        for elem in data.NuméroINE :
            if data.Classement[i] == "ECF":
                if data.SérieCode[i] == "ES":
                    dico[elem] = 100
                else :
                    dico[elem] = 0
            i+=1

    if bac == "L":
        for elem in data.NuméroINE :
            if data.Classement[i] == "ECF":
                if data.SérieCode[i] == "L":
                    dico[elem] = 100
                else :
                    dico[elem] = 0
            i+=1
    data_fin['Série (code)'] = data_fin['Numéro INE'].map(dico)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return dico

def bilan_appreciation_scientifique(nom_fichier) :
    data = pd.read_csv(nom_fichier,sep = ";")
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data = data.fillna(0)
    data.columns = data.columns.str.replace(' ', '') 
    data.columns = data.columns.str.replace('(', '') 
    data.columns = data.columns.str.replace(')', '') 
    data.columns = data.columns.str.replace("'", '_') 
    bilan = {}
    methode_de_travail = {}
    autonomie = {}
    capacite_investir = {}
    avis_capacite_reussir = {}
    avis_capacite_reussi_inv = {}
    i=0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF":
            methode_de_travail[elem] = data.MéthodedetravailCode[i]
            autonomie[elem] = data.AutonomieCode[i]
            capacite_investir[elem] = data.Capacitéàs_investirCode[i]
            avis_capacite_reussir[elem] = data.AvissurlacapacitéàréussirCode[i]
        i+=1
    for key, value in avis_capacite_reussir.items():
        avis_capacite_reussi_inv[key] = 5 - avis_capacite_reussir[key]
        bilan[key] = round(200/(methode_de_travail[key] + autonomie[key] + capacite_investir[key] + avis_capacite_reussi_inv[key]), 2)
    data_fin['Méthode de travail'] = data_fin['Numéro INE'].map(methode_de_travail)
    data_fin['Autonomie'] = data_fin['Numéro INE'].map(autonomie)
    data_fin["Capacité à s'investir"] = data_fin['Numéro INE'].map(capacite_investir)
    data_fin["Avis sur la capacité à réussir"] = data_fin['Numéro INE'].map(avis_capacite_reussi_inv)
    data_fin['Bilan appréciation'] = data_fin['Numéro INE'].map(bilan)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return bilan

def niv_classe_scientifique(nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";")
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data.columns = data.columns.str.replace(' ', '') 
    niv = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF":
            if data.Niveaudelaclasse[i] == "Bon":
                niv[elem] = 5
            elif data.Niveaudelaclasse[i] == "Très bon":
                niv[elem] = 10
            elif data.Niveaudelaclasse[i] == "Faible":
                niv[elem] = -5
            else :
                niv[elem] = 0
        i+=1
    data_fin['Bonus'] = data_fin['Numéro INE'].map(niv)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return niv

def math_premiere(poidsNoteMath, poidsClassementMath, nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";", mangle_dupe_cols = True)
    data = data.fillna(0)
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data.columns = data.columns.str.replace(' ', '') 
    data.columns = data.columns.str.replace('.', '_') 
    moy_eleve_trim1 = {}
    moy_eleve_trim2 = {}
    moy_eleve_trim3 = {}
    moy_eleve = {}
    moy_classe_trim1 = {}
    moy_classe_trim2 = {}
    moy_classe_trim3 = {}
    moy_classe = {}
    score = {}
    delta = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF" and data.NuméroINE[i] != 0:
            if pd.isna(data.MoyennecandidatenMathématiquesTrimestre1_1[i]):
                moy_eleve_trim1[elem] = 0.0
            else :
                value_trim1 = str(data.MoyennecandidatenMathématiquesTrimestre1_1[i])
                moy_eleve_trim1[elem] = float(value_trim1.replace(',', '.'))
            if pd.isna(data.MoyennecandidatenMathématiquesTrimestre2_1[i]):
                moy_eleve_trim2[elem] = 0.0
            else:
                value_trim2 = str(data.MoyennecandidatenMathématiquesTrimestre2_1[i])
                moy_eleve_trim2[elem] = float(value_trim2.replace(',', '.'))
            if pd.isna(data.MoyennecandidatenMathématiquesTrimestre3_1[i]):
                moy_eleve_trim3[elem] = 0.0
            else :
                value_trim3 = str(data.MoyennecandidatenMathématiquesTrimestre3_1[i])
                moy_eleve_trim3[elem] = float(value_trim3.replace(',', '.'))

            if pd.isna(data.MoyenneclasseenMathématiquesTrimestre1_1[i]):
                moy_classe_trim1[elem] = 0.0
            else:
                val_classe_trim1 = str(data.MoyenneclasseenMathématiquesTrimestre1_1[i])
                moy_classe_trim1[elem] = float(val_classe_trim1.replace(',', '.'))
            if pd.isna(data.MoyenneclasseenMathématiquesTrimestre2_1[i]):
                moy_classe_trim2[elem] = 0.0
            else:
                val_classe_trim2 = str(data.MoyenneclasseenMathématiquesTrimestre2_1[i])
                moy_classe_trim2[elem] = float(val_classe_trim2.replace(',', '.'))

            if pd.isna(data.MoyenneclasseenMathématiquesTrimestre3_1[i]):
                moy_classe_trim3[elem] = 0.0
            else:
                val_classe_trim3 = str(data.MoyenneclasseenMathématiquesTrimestre3_1[i])
                moy_classe_trim3[elem] = float(val_classe_trim3.replace(',', '.'))
            
            moy_eleve[elem] = round((moy_eleve_trim1[elem] + moy_eleve_trim2[elem] + moy_eleve_trim3[elem])/3, 2)                                             
            moy_classe[elem] = round((moy_classe_trim1[elem] + moy_classe_trim2[elem] + moy_classe_trim3[elem])/3, 2)
            delta[elem] = round(moy_eleve[elem] - moy_classe[elem], 2)
            score[elem] = round((poidsNoteMath*moy_eleve[elem]) + (poidsClassementMath*delta[elem]), 2)
        i+=1

    data_fin['Moyenne candidat en math (1ère)'] = data_fin['Numéro INE'].map(moy_eleve)
    data_fin['Moyenne classe en math (1ère)'] = data_fin['Numéro INE'].map(moy_classe)
    data_fin['∆ Classe Math (1ère)'] = data_fin['Numéro INE'].map(delta)
    data_fin['Points Math'] = data_fin['Numéro INE'].map(score)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return score

def PC_premiere(poidsNotePC, poidsClassementPC, nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";", mangle_dupe_cols = True)
    data = data.fillna(0)
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data.columns = data.columns.str.replace(' ', '') 
    data.columns = data.columns.str.replace('.', '_') 
    data.columns = data.columns.str.replace('/', '') 
    moy_eleve_trim1 = {}
    moy_eleve_trim2 = {}
    moy_eleve_trim3 = {}
    moy_eleve = {}
    moy_classe_trim1 = {}
    moy_classe_trim2 = {}
    moy_classe_trim3 = {}
    moy_classe = {}
    score = {}
    delta = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF" and data.NuméroINE[i] !=0:
            if pd.isna(data.MoyennecandidatenPhysiqueChimieTrimestre1_1[i]):
                moy_eleve_trim1[elem] = 0.0
            else:
                value_trim1 = str(data.MoyennecandidatenPhysiqueChimieTrimestre1_1[i])
                moy_eleve_trim1[elem] = float(value_trim1.replace(',', '.'))

            if pd.isna(data.MoyennecandidatenPhysiqueChimieTrimestre2_1[i]):
                moy_eleve_trim2[elem] = 0.0
            else:
                value_trim2 = str(data.MoyennecandidatenPhysiqueChimieTrimestre2_1[i])
                moy_eleve_trim2[elem] = float(value_trim2.replace(',', '.'))
            if pd.isna(data.MoyennecandidatenPhysiqueChimieTrimestre3_1[i]):
                moy_eleve_trim3[elem] = 0.0
            else:
                value_trim3 = str(data.MoyennecandidatenPhysiqueChimieTrimestre3_1[i])
                moy_eleve_trim3[elem] = float(value_trim3.replace(',', '.'))

            if pd.isna(data.MoyenneclasseenPhysiqueChimieTrimestre1_1[i]):
                moy_classe_trim1[elem] = 0.0
            else:
                val_classe_trim1 = str(data.MoyenneclasseenPhysiqueChimieTrimestre1_1[i])
                moy_classe_trim1[elem] = float(val_classe_trim1.replace(',', '.'))
            if pd.isna(data.MoyenneclasseenPhysiqueChimieTrimestre2_1[i]):
                moy_classe_trim2[elem] = 0.0
            else:
                val_classe_trim2 = str(data.MoyenneclasseenPhysiqueChimieTrimestre2_1[i])
                moy_classe_trim2[elem] = float(val_classe_trim2.replace(',', '.'))
            if pd.isna(data.MoyenneclasseenPhysiqueChimieTrimestre3_1[i]):
                moy_classe_trim3[elem] = 0.0
            else:
                val_classe_trim3 = str(data.MoyenneclasseenPhysiqueChimieTrimestre3_1[i])
                moy_classe_trim3[elem] = float(val_classe_trim3.replace(',', '.'))
            
            moy_eleve[elem] = round((moy_eleve_trim1[elem] + moy_eleve_trim2[elem] + moy_eleve_trim3[elem])/3, 2)
            moy_classe[elem] = round((moy_classe_trim1[elem] + moy_classe_trim2[elem] + moy_classe_trim3[elem])/3, 2)
            delta[elem] = round(moy_eleve[elem] - moy_classe[elem], 2)
            score[elem] = round((poidsNotePC*moy_eleve[elem]) + (poidsClassementPC*delta[elem]), 2)
        i+=1

    data_fin['Moyenne candidat en Physique/Chimie (1ère)'] = data_fin['Numéro INE'].map(moy_eleve)
    data_fin['Moyenne classe en Physique/Chimie (1ère)'] = data_fin['Numéro INE'].map(moy_classe)
    data_fin['∆ Classe Physique/Chimie (1ère)'] = data_fin['Numéro INE'].map(delta)
    data_fin['Points Physique/Chimie'] = data_fin['Numéro INE'].map(score)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return score

def SVT_premiere(poidsNoteSVT, poidsClassementSVT, nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";", mangle_dupe_cols = True)
    data = data.fillna(0)
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data.columns = data.columns.str.replace(' ', '') 
    data.columns = data.columns.str.replace('.', '_') 
    moy_eleve_trim1 = {}
    moy_eleve_trim2 = {}
    moy_eleve_trim3 = {}
    moy_eleve = {}
    moy_classe_trim1 = {}
    moy_classe_trim2 = {}
    moy_classe_trim3 = {}
    moy_classe = {}
    score = {}
    delta = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF" and data.NuméroINE[i] != 0:
            if pd.isna(data.MoyennecandidatenSciencesdelaVieetdelaTerreTrimestre1_1[i]):
                moy_eleve_trim1[elem] = 0.0
            else:
                value_trim1 = str(data.MoyennecandidatenSciencesdelaVieetdelaTerreTrimestre1_1[i])
                moy_eleve_trim1[elem] = float(value_trim1.replace(',', '.'))
            if pd.isna(data.MoyennecandidatenSciencesdelaVieetdelaTerreTrimestre2_1[i]):
                moy_eleve_trim2[elem] = 0.0
            else:
                value_trim2 = str(data.MoyennecandidatenSciencesdelaVieetdelaTerreTrimestre2_1[i])
                moy_eleve_trim2[elem] = float(value_trim2.replace(',', '.'))
            if pd.isna(data.MoyennecandidatenSciencesdelaVieetdelaTerreTrimestre3_1[i]):
                moy_eleve_trim3[elem] = 0.0
            else:
                value_trim3 = str(data.MoyennecandidatenSciencesdelaVieetdelaTerreTrimestre3_1[i])
                moy_eleve_trim3[elem] = float(value_trim3.replace(',', '.'))

            if pd.isna(data.MoyenneclasseenSciencesdelaVieetdelaTerreTrimestre1_1[i]):
                moy_classe_trim1[elem] = 0.0
            else:
                val_classe_trim1 = str(data.MoyenneclasseenSciencesdelaVieetdelaTerreTrimestre1_1[i])
                moy_classe_trim1[elem] = float(val_classe_trim1.replace(',', '.'))
            if pd.isna(data.MoyenneclasseenSciencesdelaVieetdelaTerreTrimestre2_1[i]):
                moy_classe_trim2[elem] = 0.0
            else:
                val_classe_trim2 = str(data.MoyenneclasseenSciencesdelaVieetdelaTerreTrimestre2_1[i])
                moy_classe_trim2[elem] = float(val_classe_trim2.replace(',', '.'))
            if pd.isna(data.MoyenneclasseenSciencesdelaVieetdelaTerreTrimestre3_1[i]):
                moy_classe_trim3[elem] = 0.0
            else:
                val_classe_trim3 = str(data.MoyenneclasseenSciencesdelaVieetdelaTerreTrimestre3_1[i])
                moy_classe_trim3[elem] = float(val_classe_trim3.replace(',', '.'))

            moy_eleve[elem] = round((moy_eleve_trim1[elem] + moy_eleve_trim2[elem] + moy_eleve_trim3[elem])/3, 2)
            moy_classe[elem] = round((moy_classe_trim1[elem] + moy_classe_trim2[elem] + moy_classe_trim3[elem])/3, 2)
            delta[elem] = round(moy_eleve[elem] - moy_classe[elem], 2)
            score[elem] = round((poidsNoteSVT*moy_eleve[elem]) + (poidsClassementSVT*delta[elem]), 2)
        i+=1

    data_fin['Moyenne candidat en SVT (1ère)'] = data_fin['Numéro INE'].map(moy_eleve)
    data_fin['Moyenne classe en SVT (1ère)'] = data_fin['Numéro INE'].map(moy_classe)
    data_fin['∆ Classe SVT (1ère)'] = data_fin['Numéro INE'].map(delta)
    data_fin['Points SVT'] = data_fin['Numéro INE'].map(score)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return score

def total_premiere_scientifique(listeMatiere, poidsNoteMath, poidsClassementMath, poidsNotePC, poidsClassementPC, poidsNoteSVT, poidsClassementSVT, fichier):
    data = pd.read_csv(fichier,sep = ";", mangle_dupe_cols = True)
    data.columns = data.columns.str.replace(' ', '') 
    data = data.fillna(0)
    liste = []
    for matiere in listeMatiere:
        if matiere == "Math":
            liste.append(math_premiere(poidsNoteMath, poidsClassementMath, fichier))
        elif matiere == "PC":
            liste.append(PC_premiere(poidsNotePC, poidsClassementPC, fichier))
        elif matiere == "SVT":
            liste.append(SVT_premiere(poidsNoteSVT, poidsClassementSVT, fichier))
    total = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF" and data.NuméroINE[i] != 0:
            total[elem] = 0
        i+=1
    if liste:
        for matiere in liste :
            for key in matiere :
                total[key] = round(total[key] + matiere[key], 2)
    return total

def math_terminal(poidsNoteMath, poidsClassementMath, nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";")
    data = data.fillna(0)
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data.columns = data.columns.str.replace(' ', '')
    data.columns = data.columns.str.replace('(', '')
    data.columns = data.columns.str.replace(')', '')
    data.columns = data.columns.str.replace('/', '')
    moy_eleve = {}
    moy_classe = {}
    score = {}
    delta = {}
    point_rang = {}
    classement = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF" and data.NuméroINE[i] != 0:
            if pd.isna(data.MoyennecandidatenMathématiquesTrimestre1[i]):
                moy_eleve[elem] = 0.0
            else :
                value_trim1 = str(data.MoyennecandidatenMathématiquesTrimestre1[i])
                moy_eleve[elem] = float(value_trim1.replace(',', '.'))

            if pd.isna(data.MoyenneclasseenMathématiquesTrimestre1[i]):
                moy_classe[elem] = 0.0
            else:
                val_classe_trim1 = str(data.MoyenneclasseenMathématiquesTrimestre1[i])
                moy_classe[elem] = float(val_classe_trim1.replace(',', '.'))

            if pd.isna(data.ClassementMathématiques[i]):
                classement[elem] = 0
            else :
                classement[elem] = int(data.ClassementMathématiques[i])
            
            if classement[elem] != 0:
                point_rang[elem] = 30 - classement[elem]
            else :
                point_rang[elem] = 0

            delta[elem] = round(moy_eleve[elem] - moy_classe[elem], 2)
            score[elem] = round((poidsNoteMath*moy_eleve[elem]) + (poidsClassementMath*delta[elem]) + point_rang[elem], 2)
        i+=1

    data_fin['Note étudiant Math'] = data_fin['Numéro INE'].map(moy_eleve)
    data_fin['∆ Classe Math'] = data_fin['Numéro INE'].map(delta)
    data_fin['Point rang (Mathématiques)'] = data_fin['Numéro INE'].map(point_rang)
    data_fin['Math Terminale'] = data_fin['Numéro INE'].map(score)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return score

def pc_terminal(poidsNotePC, poidsClassementPC, nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";")
    data = data.fillna(0)
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data.columns = data.columns.str.replace(' ', '')
    data.columns = data.columns.str.replace('(', '')
    data.columns = data.columns.str.replace(')', '')
    data.columns = data.columns.str.replace('/', '')
    moy_eleve = {}
    moy_classe = {}
    score = {}
    delta = {}
    point_rang = {}
    classement = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF" and data.NuméroINE[i] != 0:
            if pd.isna(data.MoyennecandidatenPhysiqueChimieTrimestre1[i]):
                moy_eleve[elem] = 0.0
            else :
                value_trim1 = str(data.MoyennecandidatenPhysiqueChimieTrimestre1[i])
                moy_eleve[elem] = float(value_trim1.replace(',', '.'))

            if pd.isna(data.MoyenneclasseenPhysiqueChimieTrimestre1[i]):
                moy_classe[elem] = 0.0
            else:
                val_classe_trim1 = str(data.MoyenneclasseenPhysiqueChimieTrimestre1[i])
                moy_classe[elem] = float(val_classe_trim1.replace(',', '.'))

            if pd.isna(data.ClassementPhysiqueChimie[i]):
                classement[elem] = 0.0
            else :
                classement[elem] = data.ClassementPhysiqueChimie[i]
            
            if classement[elem] != 0.0:
                point_rang[elem] = 30 - classement[elem]
            else :
                point_rang[elem] = 0.0

            delta[elem] = round(moy_eleve[elem] - moy_classe[elem], 2)
            score[elem] = round((poidsNotePC*moy_eleve[elem]) + (poidsClassementPC*delta[elem]) + point_rang[elem], 2)
        i+=1

    data_fin['Note étudiant Physique/Chimie'] = data_fin['Numéro INE'].map(moy_eleve)
    data_fin['∆ Classe Physique/Chimie'] = data_fin['Numéro INE'].map(delta)
    data_fin['Point rang (Physique/Chimie)'] = data_fin['Numéro INE'].map(point_rang)
    data_fin['Physique/Chimie Terminale'] = data_fin['Numéro INE'].map(score)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return score

def svt_terminal(poidsNoteSVT, poidsClassementSVT, nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";")
    data = data.fillna(0)
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data.columns = data.columns.str.replace(' ', '')
    data.columns = data.columns.str.replace('(', '')
    data.columns = data.columns.str.replace(')', '')
    data.columns = data.columns.str.replace('/', '')
    moy_eleve = {}
    moy_classe = {}
    score = {}
    delta = {}
    point_rang = {}
    classement = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF" and data.NuméroINE[i] != 0:
            if pd.isna(data.MoyennecandidatenSciencesdelaVieetdelaTerreTrimestre1[i]):
                moy_eleve[elem] = 0.0
            else :
                value_trim1 = str(data.MoyennecandidatenSciencesdelaVieetdelaTerreTrimestre1[i])
                moy_eleve[elem] = float(value_trim1.replace(',', '.'))

            if pd.isna(data.MoyenneclasseenSciencesdelaVieetdelaTerreTrimestre1[i]):
                moy_classe[elem] = 0.0
            else:
                val_classe_trim1 = str(data.MoyenneclasseenSciencesdelaVieetdelaTerreTrimestre1[i])
                moy_classe[elem] = float(val_classe_trim1.replace(',', '.'))

            if pd.isna(data.ClassementSciencesdelaVieetdelaTerre[i]):
                classement[elem] = 0.0
            else :
                classement[elem] = data.ClassementSciencesdelaVieetdelaTerre[i]
            
            if classement[elem] != 0.0:
                point_rang[elem] = 30 - classement[elem]
            else :
                point_rang[elem] = 0.0

            delta[elem] = round(moy_eleve[elem] - moy_classe[elem], 2)
            score[elem] = round((poidsNoteSVT*moy_eleve[elem]) + (poidsClassementSVT*delta[elem]) + point_rang[elem], 2)
        i+=1

    data_fin['Note étudiant SVT'] = data_fin['Numéro INE'].map(moy_eleve)
    data_fin['∆ Classe SVT'] = data_fin['Numéro INE'].map(delta)
    data_fin['Point rang (SVT)'] = data_fin['Numéro INE'].map(point_rang)
    data_fin['SVT Terminale'] = data_fin['Numéro INE'].map(score)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return score

def total_terminale_scientifique(listeMatiere, poidsNoteMath, poidsClassementMath, poidsNotePC, poidsClassementPC, poidsNoteSVT, poidsClassementSVT, fichier):
    data = pd.read_csv(fichier,sep = ";", mangle_dupe_cols = True)
    data.columns = data.columns.str.replace(' ', '') 
    data = data.fillna(0)
    liste = []
    for matiere in listeMatiere:
        if matiere == "Math":
            liste.append(math_terminal(poidsNoteMath, poidsClassementMath, fichier))
        elif matiere == "PC":
            liste.append(pc_terminal(poidsNotePC, poidsClassementPC, fichier))
        elif matiere == "SVT":
            liste.append(svt_terminal(poidsNoteSVT, poidsClassementSVT, fichier))
    total = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF" and data.NuméroINE[i] != 0:
            total[elem] = 0
        i+=1
    if liste:
        for matiere in liste :
            for key in matiere :
                total[key] = round(total[key] + matiere[key], 2)
    return total

def note_bac_prem_scientifique(nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";", mangle_dupe_cols = True)
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data = data.fillna(0)
    data.columns = data.columns.str.replace(' ', '') 
    data.columns = data.columns.str.replace('(', '') 
    data.columns = data.columns.str.replace(')', '') 
    data.columns = data.columns.str.replace("'", '')  
    tpe = {}
    oral_fr = {}
    ecrit_fr = {}
    total = {}
    i = 0
    for elem in data.NuméroINE :
        if data.Classement[i] == "ECF":
            tpe[elem] = data.NoteàlépreuvedeTravauxPersonnelsEncadrésépreuveanticipée[i]
            oral_fr[elem] = data.NoteàlépreuvedeOraldeFrançaisépreuveanticipée[i]
            ecrit_fr[elem] = data.NoteàlépreuvedeEcritdeFrançaisépreuveanticipée[i]
            total[elem] = tpe[elem] + oral_fr[elem] + ecrit_fr[elem]
        i+=1
    data_fin['Français Oral Bac'] = data_fin['Numéro INE'].map(oral_fr)
    data_fin['Français Ecrit Bac'] = data_fin['Numéro INE'].map(ecrit_fr)
    data_fin['TPE'] = data_fin['Numéro INE'].map(tpe)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return total

def bilan_total_scientifique(listeMatiere, poidsNoteMath, poidsClassementMath, poidsNotePC, poidsClassementPC, poidsNoteSVT, poidsClassementSVT, bac, nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";")
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data = data.fillna(0)
    data.columns = data.columns.str.replace(' ', '')
    data.columns = data.columns.str.replace('(', '') 
    data.columns = data.columns.str.replace(')', '')
    with open('res_mat_scientifique.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow(('Numéro INE', 'Nom', 'Lycée', 'Bac'))
        i = 0
        for elem in data.NuméroINE :
            if data.Classement[i] == "ECF" and data.NuméroINE[i] != 0:
                writer.writerow((elem, data.Nom[i], data.Libelléétablissement[i], data.SérieCode[i]))
            i+=1

    score_finale = {}
    score_term = {}
    total_term = {}
    total_moy_ter = total_terminale_scientifique(listeMatiere, poidsNoteMath, poidsClassementMath, poidsNotePC, poidsClassementPC, poidsNoteSVT, poidsClassementSVT, nom_fichier)
    total_prem = total_premiere_scientifique(listeMatiere, poidsNoteMath, poidsClassementMath, poidsNotePC, poidsClassementPC, poidsNoteSVT, poidsClassementSVT, nom_fichier)
    points_bac = prio_bac(bac, nom_fichier)
    bilan_apprec = bilan_appreciation_scientifique(nom_fichier)
    bonus_classe = niv_classe_scientifique(nom_fichier)
    note_bac_premiere = note_bac_prem_scientifique(nom_fichier)
    for key in total_moy_ter:
        score_term[key] = round((note_bac_premiere[key]/2) + total_moy_ter[key], 2)
        total_term[key] = round(score_term[key] + bilan_apprec[key] + points_bac[key], 2)
        score_finale[key] = round((total_term[key] + (total_prem[key]/2)) + bonus_classe[key], 2)
    data_fin = pd.read_csv("res_mat_scientifique.csv", sep = ";")
    data_fin['Total terminale'] = data_fin['Numéro INE'].map(total_term)
    data_fin['Bilan Total'] = data_fin['Numéro INE'].map(score_finale)
    data_fin.to_csv("res_mat_scientifique.csv", sep = ";", index = False)
    return score_finale

def dico_final(nom_fichier):
    data = pd.read_csv(nom_fichier,sep = ";")
    data.columns = data.columns.str.replace(' ', '')
    data = data.set_index('NuméroINE').T.to_dict('list')
    return data