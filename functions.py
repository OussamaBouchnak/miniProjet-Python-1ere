import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import os
import re
import datetime

fichier = "students.csv"
header = ['Numero_inscription', 'Nom', 'Prenom', 'Date', 'Niveau', 'Section', 'Mail', 'Telephone', 'Adresse']
fichier2 = "livres.csv"
header2 = ['reference', 'titre', 'auteur', 'annee','nombre_exemplaires']
fichier3 = "emprunts.csv"
header3= ['Numero_inscription','reference','date_emp','date_retour']
def passwd(window):
    nom= window.user.text()
    passwd = window.mdp.text()
    if (passwd == "oussama1" and nom == "oussama"):
        window.acceuil.setEnabled(True)
        window.gest_livre.setEnabled(True)
        window.enreg_recup.setEnabled(True)
        window.gest_emp.setEnabled(True)
        window.user.setText("")
        window.mdp.setText("")
    else :
        show_err("nom d'utilisateur ou mot de passe incorrect")
        window.user.setText("")
        window.mdp.setText("")
def show_err(ch):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    msg_box.setWindowTitle("Erreur")
    msg_box.setText(ch)
    msg_box.exec_()
def show_msg(ch):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Information)
    msg_box.setWindowTitle("Succès")
    msg_box.setText(ch)
    msg_box.exec_()
def valid_date(date):
    try:
        d = datetime.datetime.strptime(date, "%d/%m/%Y")
        now = datetime.datetime.now()
        
        if  now > d:
            return True, "date valide"
        else:
            return False, "la date de naissance doit etre inférieure à celle d'aujoudhui !"
    except ValueError:
        return False, "date invalide (verifiez le format jj/mm/aa)"
def valid_date1(emp,ret):
    try:
        e = datetime.datetime.strptime(emp, "%d/%m/%Y")
        r = datetime.datetime.strptime(ret, "%d/%m/%Y")
        now = datetime.datetime.now()
        
        if  now > e and r > e:
            return True, "date valide"
        elif now < e:
            return False, "la date d'emprunte doit etre inférieure à celle d'aujoudhui !"
        else :
            return False, "la date d'emprunte doit etre inférieure à celle de retour !"
    except ValueError:
        return False, "date invalide (verifiez le format jj/mm/aa)"
def valid_date_emp(emp1,emp2,ret):
    try:
        e1 = datetime.datetime.strptime(emp1, "%d/%m/%Y")
        e2 = datetime.datetime.strptime(emp2, "%d/%m/%Y")
        r = datetime.datetime.strptime(ret, "%d/%m/%Y")
        now = datetime.datetime.now()
        
        if  now >= e1 and now >= e2 and e1 != e2 and r > e2:
            return True, "date valide"
        elif now < e1 or now < e2:
            return False, "la date d'emprunte doit etre inférieure à celle d'aujoudhui !"
        elif e2>= r:
            return False, "la date d'emprunte doit etre inférieure à celle de retour !"
        else :
            return False, "donner une date différente de l'ancienne !"
    except ValueError:
        return False, "date invalide (verifiez le format jj/mm/aa)"
def valid_date_ret(ret1,ret2,emp):
    try:
        r1 = datetime.datetime.strptime(ret1, "%d/%m/%Y")
        r2 = datetime.datetime.strptime(ret2, "%d/%m/%Y")
        e = datetime.datetime.strptime(emp, "%d/%m/%Y")
        if r1 != r2 and r2 > e:
            return True, "date valide"
        elif r2 <= e:
            return False, "la date de retour doit etre supérieure à celle d'aujoudhui !"
        else :
            return False, "donner une date différente !"
    except ValueError:
        return False, "date invalide (verifiez le format jj/mm/aa)"

def valid_date2(date):
    try:
        d = datetime.datetime.strptime(date, "%d/%m/%Y")
        now = datetime.datetime.now()
        return True , "date valide"
    except ValueError:
        return False, "date invalide (verifiez le format jj/mm/aa)"
def valid_2date_emp(date1,date2):
    try:
        date1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
        date2 = datetime.datetime.strptime(date2, "%d/%m/%Y")
        now = datetime.datetime.now()
        
        if  now > date2 > date1 :
            return True, "dates valides"
        elif now < date1 or now < date2 :
            return False, "la date d'emprunte doit etre inférieure à celle d'aujoudhui !"
        else :
            return False, "la 1ere date doit etre inférieure à la 2eme"
    except ValueError:
        return False, "date invalide (verifiez le format jj/mm/aa)"
    
def valid_2date_ret(date1,date2):
    try:
        date1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
        date2 = datetime.datetime.strptime(date2, "%d/%m/%Y")
        now = datetime.datetime.now()
        
        if  now > date2 > date1:
            return True, "dates valides"
        else :
            return False, "la 1ere date doit etre inférieure à la 2eme"
    except ValueError:
        return False, "date invalide (verifiez le format jj/mm/aa)"
def cin_verif(cin):
    if len(cin) == 8 and cin.isdigit():
        if os.fichier.exists(fichier) and os.fichier.getsize(fichier) > 0:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['CIN'] == cin]
                if rows:
                    return True
                else:
                    return False
                
                
def add_student(window_add_student):
    numero_inscription = window_add_student.inscri.text()
    nom = window_add_student.nom.text()
    prenom = window_add_student.prenom.text()
    mail = window_add_student.mail.text()
    adresse = window_add_student.adresse.text()
    niveau = window_add_student.niv.text()
    telephone = window_add_student.tel.text()
    date_naissance = window_add_student.date.text()
    section = window_add_student.section.text()
    verif_date,date_err= valid_date(date_naissance)
    err = ""
    if len(numero_inscription)!=8 or numero_inscription.isdigit()==False :
        err=err+"Verifier le Numéro d'inscription\n"
    if len(nom)<3:
        err=err+"Verifier le nom\n"
    if len(prenom)<3 or prenom.isalpha()==False :
        err=err+"Verifier le prenom\n"
    if len(adresse)<3 or adresse.isalpha()==False :
        err=err+"Verifier l'adresse\n"
    if len(telephone)!=8 or telephone.isdigit()==False :
        err=err+"Verifier le numero de téléphone\n"   
    if not verif_date:
        err=err+date_err+'\n'
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(regex, mail):
        err=err+"Verifier l'adresse mail\n"
    if section=="":
        err=err+"Verifier la section\n"
    if niveau=="" or niveau == '0':
        err=err+"Verifier le niveau\n"

    
    if err:
        QtWidgets.QMessageBox.critical(None, "Erreur", err)
        return
    date_naissance = datetime.datetime.strptime(date_naissance, "%d/%m/%Y").date()
    # Create a dictionary with the new person's data
    student_dict = {
        'Numero_inscription': numero_inscription,
        'Nom': nom,
        'Prenom': prenom,
        'Date': date_naissance,
        'Niveau': niveau,
        'Section' : section,
        'Mail': mail,
        'Telephone': telephone,
        'Adresse': adresse,
    }

    # Write the dictionary to the CSV file
    with open(fichier, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=student_dict.keys())
        if os.stat(fichier).st_size == 0:
            writer.writeheader()
        else:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = [row for row in reader if row['Numero_inscription'] == numero_inscription]
            if rows:
                show_err("Le Numero d'inscription existe déjà")
                return

        writer.writerow(student_dict)
    window_add_student.inscri.setText("")
    window_add_student.nom.setText("")
    window_add_student.prenom.setText("")
    window_add_student.mail.setText("")
    window_add_student.adresse.setText("")
    window_add_student.niv.setText("")
    window_add_student.tel.setText("")
    window_add_student.date.setText("")
    window_add_student.section.setText("")
    show_msg("Etudiant ajouté avec succès")
  
def delete(window_Supp):
    num = window_Supp.num.text()
    if len(num) == 8 and num.isdigit():
        if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['Numero_inscription'] != num]
                f.seek(0)
                rows1 = [row for row in reader if row['Numero_inscription'] == num]
            if rows1 :
                with open(fichier, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    for row in rows:
                        writer.writerow(row.values())

                    window_Supp.num.setText("")
                    show_msg("Etudiant supprimé avec succès")
            else:
                show_err("Le Numero d'inscription n'existe pas")
        else:
            show_err("Le fichier des étudiants est vide")
    else:
        show_err("Numero d'inscription invalide")
def supprimer_livre(window_Supp):
    ref = window_Supp.lineEdit.text()
    if ref.isdigit():
        if os.path.exists(fichier2) and os.path.getsize(fichier2) > 0:
            with open(fichier2, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['reference'] != ref]
                f.seek(0)
                rows1 = [row for row in reader if row['reference'] == ref]
            if rows1 :
                with open(fichier2, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header2)
                    for row in rows:
                        writer.writerow(row.values())

                    window_Supp.lineEdit.setText("")
                    show_msg("livre supprimé avec succès")
            else:
                show_err("le livre n'existe pas")
        else:
            show_err("Le fichier des livre est vide")
    else:
        show_err("référence invalide")
def supprimer_section(window_Supp_sec):
    section = window_Supp_sec.section.text()
    if (section != ""):
        if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['Section'].upper() != section.upper().upper()]
                f.seek(0)
                rows1 = [row for row in reader if row['Section'].upper() == section.upper().upper()]
            if rows1 :
                with open(fichier, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    for row in rows:
                        writer.writerow(row.values())

                    window_Supp_sec.section.setText("")
                    show_msg("section supprimée avec succès")
            else:
                show_err("la section n'existe pas")
        else:
            show_err("Le fichier des étudiants est vide")
    else:
        show_err("Section invalide")

def supprimer_niveau(window_Supp_niv):
    niveau = window_Supp_niv.niveau.text()
    if (niveau != ""):
        if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['Niveau'] != niveau]
                f.seek(0)
                rows1 = [row for row in reader if row['Niveau'] == niveau]
            if rows1 :
                with open(fichier, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    for row in rows:
                        writer.writerow(row.values())

                    window_Supp_niv.niveau.setText("")
                    show_msg("niveau supprimé avec succès")
            else:
                show_err("le niveau n'existe pas")
        else:
            show_err("Le fichier des étudiants est vide")
    else:
        show_err("niveau invalide")

def supprimer_section_niveau(window_Supp_sec_niv):
    section = window_Supp_sec_niv.section.text()
    niveau = window_Supp_sec_niv.niveau.text()
    if (niveau != "" and  section != ""):
        if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['Section'].upper() != section.upper() or row['Niveau'] != niveau]
                f.seek(0)
                rows1 = [row for row in reader if row['Section'].upper() == section.upper() and row['Niveau'] == niveau]
            if rows1 :
                with open(fichier, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    for row in rows:
                        writer.writerow(row.values())

                    window_Supp_sec_niv.section.setText("")
                    window_Supp_sec_niv.niveau.setText("")
                    show_msg("suppression avec succès")
            else:
                show_err("les données que vous avez fourni n'existent pas")
        else:
            show_err("Le fichier des étudiants est vide")
    else:
        if section == "":
            show_err("Section invalide")
        else :
            show_err("Niveau invalide")
        
def affichage(window_show_contenu):
    if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
        model = QStandardItemModel()
        model.clear()
        df = pd.read_csv('students.csv')
        model.setHorizontalHeaderLabels(header) 
        for row in range(df.shape[0]):
            model.insertRow(row)
            for col in range(df.shape[1]):
                item = QStandardItem(str(df.iloc[row, col]))
                model.setItem(row, col, item)
        window_show_contenu.tableView.setModel(model)
    else:
        show_err("Le fichier des étudiants est vide")
   
def affichage_livre(window_show_contenu):
    if os.path.exists(fichier2) and os.path.getsize(fichier2) > 0:
        model = QStandardItemModel()
        model.clear()
        df = pd.read_csv('livres.csv')
        model.setHorizontalHeaderLabels(header2) 
        for row in range(df.shape[0]):
            model.insertRow(row)
            for col in range(df.shape[1]):
                item = QStandardItem(str(df.iloc[row, col]))
                model.setItem(row, col, item)
        window_show_contenu.tableView.setModel(model)
    else:
        show_err("Le fichier des livres est vide")
def annuler (window):
    model = QStandardItemModel() 
    model.clear() 
    window.tableView.setModel(model)
    window.close()
def annuler1 (window):
    window.lineEdit.setText("")
    window.lineEdit_2.setText("")
    window.lineEdit_3.setText("")
    window.lineEdit_4.setText("")
    window.close()
def annuler2 (window):
    window.lineEdit.setText("")
    window.close() 
def affichage1(window_show_contenu):
    if os.path.exists(fichier3) and os.path.getsize(fichier3) > 0:
        model = QStandardItemModel()
        model.clear()
        df = pd.read_csv('emprunts.csv')
        model.setHorizontalHeaderLabels(header3) 
        for row in range(df.shape[0]):
            model.insertRow(row)
            for col in range(df.shape[1]):
                item = QStandardItem(str(df.iloc[row, col]))
                model.setItem(row, col, item)
        window_show_contenu.tableView.setModel(model)
    else:
        show_err("Le fichier des emprunts est vide")
    
   
    
def modifier_telephone(window_mod_tel):
    num,telephone = window_mod_tel.lineEdit.text() , window_mod_tel.lineEdit_2.text()
    if (len(num)==8 or num.isdigit()==True) and (len(telephone)==8 or telephone.isdigit()==True):
        if(os.path.exists(fichier) and os.path.getsize(fichier) > 0):
            with open(fichier, 'r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            found = False
            for row in rows:
                if row['Numero_inscription'] == num:
                    row['Telephone'] = telephone
                    found = True
                    break

            if found:
                with open(fichier, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                show_msg(f"Téléphone de l'étudiant ayant le numéro d'inscription {num} a été modifié")
            else:
                show_err(f"l'étudiant ayant le numéro d'inscription {num} n'existe pas")
        else:
            show_err("le fichier des étudiants est vide ou n'existe pas")
    else:
        show_err("Vérifier le numéro d'inscription ou le numéro de téléphone ")
    window_mod_tel.lineEdit.setText('')
    window_mod_tel.lineEdit_2.setText("")

def modifier_adresse(window):
    num, adresse = window.lineEdit.text(), window.lineEdit_2.text()
    if (len(num) == 8 or num.isdigit() == True) and (len(adresse) > 3 or adresse.isalpha() == True):
        if(os.path.exists(fichier) and os.path.getsize(fichier) > 0):
            with open(fichier, 'r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            found = False
            for row in rows:
                if row['Numero_inscription'] == num:
                    row['Adresse'] = adresse
                    found = True
                    break

            if found:
                with open(fichier, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                show_msg(f"l'adresse de l'étudiant ayant le numéro d'inscription {num} a été modifiée")
            else:
                show_err(f"l'étudiant ayant le numéro d'inscription {num} n'existe pas")
        else:
            show_err("le fichier des étudiants est vide ou n'existe pas")
    else:
        show_err("Vérifier le numéro d'inscription ou l'adresse ")
    window.lineEdit.setText('')
    window.lineEdit_2.setText("")
def modifier_mail(window):
    num, mail = window.lineEdit.text(), window.lineEdit_2.text()
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if (len(num) == 8 or num.isdigit() == True)  and re.match(regex, mail):
        if(os.path.exists(fichier) and os.path.getsize(fichier) > 0):
            with open(fichier, 'r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            found = False
            for row in rows:
                if row['Numero_inscription'] == num:
                    row['Mail'] = mail
                    found = True
                    break

            if found:
                with open(fichier, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                show_msg(f"l'adresse mail de l'étudiant ayant le numéro d'inscription {num} a été modifiée")
            else:
                show_err(f"l'étudiant ayant le numéro d'inscription {num} n'existe pas")
        else:
            show_err("le fichier des étudiants est vide ou n'existe pas")
    else:
        show_err("Vérifier le numéro d'inscription ou l'adresse mail ")
    window.lineEdit.setText('')
    window.lineEdit_2.setText("")


def recherche_niv (window_rech_niv):
    niv = window_rech_niv.lineEdit.text()
    if (niv != "" and niv != '0'):
        if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['Niveau'] == niv:
                        rows.append(row)

                if rows:
                    fieldnames = ['Numero_inscription', 'Nom', 'Prenom', 'Date', 'Niveau', 'Section', 'Mail', 'Telephone', 'Adresse']
                    model = CsvTableModelDict(rows, fieldnames)
                    window_rech_niv.tableView.setModel(model)
                    window_rech_niv.lineEdit.setText("")
                else:
                    window_rech_niv.tableView.setModel(None)
                    show_err("Aucun résultat trouvé pour ce niveau")
        else:
            window_rech_niv.tableView.setModel(None)
            show_err("le fichier etudiants est vide ou n'existe pas")
    else:
        window_rech_niv.tableView.setModel(None)
        show_err("Vérifier le niveau donné")

def recherche_sec (window_rech_sec):
    sec = window_rech_sec.lineEdit.text()
    if (sec != ""):
        if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
    
                    if row['Section'].upper() == sec.upper():
                        rows.append(row)

                if rows:
                    fieldnames = ['Numero_inscription', 'Nom', 'Prenom', 'Date', 'Niveau', 'Section', 'Mail', 'Telephone', 'Adresse']
                    model = CsvTableModelDict(rows, fieldnames)
                    window_rech_sec.tableView.setModel(model)
                    window_rech_sec.lineEdit.setText("")
                else:
                    window_rech_sec.tableView.setModel(None)
                    show_err("Aucun résultat trouvé pour cette section")
        else:
            window_rech_sec.tableView.setModel(None)
            show_err("le fichier etudiants est vide ou n'existe pas")
    else:
        window_rech_sec.tableView.setModel(None)
        show_err("Vérifier la section donné")

def recherche_sec_niv (window_rech_sec_niv):
    sec = window_rech_sec_niv.lineEdit.text()
    niv = window_rech_sec_niv.lineEdit_2.text()
    if (sec != "" and niv != ""):
        if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['Section'].upper() == sec.upper() and row['Niveau'] == niv:
                        rows.append(row)

                if rows:
                    fieldnames = ['Numero_inscription', 'Nom', 'Prenom', 'Date', 'Niveau', 'Section', 'Mail', 'Telephone', 'Adresse']
                    model = CsvTableModelDict(rows, fieldnames)
                    window_rech_sec_niv.tableView.setModel(model)
                    window_rech_sec_niv.lineEdit.setText("")
                    window_rech_sec_niv.lineEdit_2.setText("")
                else:
                    window_rech_sec_niv.tableView.setModel(None)
                    show_err("Aucun résultat trouvé pour ce niveau de cette section")
        else:
            window_rech_sec_niv.tableView.setModel(None)
            show_err("le fichier etudiants est vide ou n'existe pas")
    else:
        window_rech_sec_niv.tableView.setModel(None)
        if sec == "" and niv == "":
            show_err("Vérifier la section et le niveau ")
        elif niv == "" :
            show_err("Vérifier le niveau ")
        else :
            show_err("Vérifier la section ")
def recherche_num (window_rech_num):
    num = window_rech_num.lineEdit.text()
    if (len(num)==8 or num.isdigit()==True):
        if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['Numero_inscription'] == num :
                        rows.append(row)

                if rows:
                    fieldnames = ['Numero_inscription', 'Nom', 'Prenom', 'Date', 'Niveau', 'Section', 'Mail', 'Telephone', 'Adresse']
                    model = CsvTableModelDict(rows, fieldnames)
                    window_rech_num.tableView.setModel(model)
                    window_rech_num.lineEdit.setText("")
                else:
                    window_rech_num.tableView.setModel(None)
                    show_err("Aucun résultat trouvé pour ce numero d'inscription")
        else:
            window_rech_num.tableView.setModel(None)
            show_err("le fichier etudiants est vide ou n'existe pas")
    else:
        window_rech_num.tableView.setModel(None)
        show_err("numéro d'inscription invalide")
                        
class CsvTableModelDict(QtCore.QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        super().__init__(parent)
        self._data = data
        self._header = header

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._header)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            try:
                return str(self._data[row][self._header[col]])
            except KeyError:
                return None

def ajout_livre(window):
    
    ref= window.lineEdit.text()
    titre = window.lineEdit_2.text()
    auteur = window.lineEdit_3.text()
    annee = window.lineEdit_4.text()
    nb = window.lineEdit_5.text()
    err = ""
    if not ref.isnumeric():
        err += "Vérifier la référence du livre\n"
    if not nb.isnumeric():
        err += "Vérifier le nombre d'exemplaires\n"
    if titre == "" :
        err += "Vérifier le titre\n"
    if  auteur == "":
        err += "Vérifier l'auteur\n"
    if not annee.isnumeric() or not 1800<=int(annee)<=2023 :
        err += "Vérifier l'année d'édition \n"
        
    if err:
        show_err(err)
        return

    livre = {
        'reference': ref,
        'titre': titre,
        'auteur': auteur,
        'annee': annee,
        'nombre_exemplaires' : int(nb),
    }

    with open(fichier2, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=livre.keys())
        if os.stat(fichier2).st_size == 0:
            writer.writeheader()
        writer.writerow(livre)

    show_msg("livre ajouté avec succès !")

def ajout_emp(window):
    
    if os.path.exists(fichier2) and os.path.getsize(fichier2) > 0 and os.path.exists(fichier) and os.path.getsize(fichier) > 0:
        num= window.lineEdit.text()
        ref = window.lineEdit_2.text()
        date_emp = window.lineEdit_3.text()
        date_retour = window.lineEdit_4.text()
        
        verif_date,date_err= valid_date1(date_emp,date_retour)
        err = ""
        if len(num)!=8 or num.isdigit()==False :
            err=err+"Verifier le Numéro d'inscription\n"
        else :
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)

                f.seek(0)
                rows1 = [row for row in reader if row['Numero_inscription'] == num]
            if not rows1 :
                err += "le numéro d'inscription n'exisite pas\n"
        if not ref.isnumeric():
            err += "Vérifier la référence du livre\n"
        else :
            with open(fichier2, 'r', newline='') as f:
                reader = csv.DictReader(f)

                f.seek(0)
                rows2 = [row for row in reader if row['reference'] == ref and int(row['nombre_exemplaires']) > 0]
            if not rows2 :
                err += "le livre n'exisite pas ouil n'ya pas suffisament d'exemplaires\n"
            
        if not verif_date:
            err=err+date_err+'\n'
        
    else :
        err += "l'un des fichiers est vide ! \n"
    if err:
        show_err(err)
        return
    emprunte = {
        'Numero_inscription': num,
        'reference': ref,
        'date_emp': date_emp,
        'date_retour': date_retour,
    }

    with open(fichier3, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=emprunte.keys())
        if os.stat(fichier3).st_size == 0:
            writer.writeheader()
        writer.writerow(emprunte)
    with open(fichier2, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    for row in rows:
        if row['reference'] == ref:
            row['nombre_exemplaires']=int(row['nombre_exemplaires'])-1
            break
    with open(fichier2, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    show_msg("Emprunte ajoutée avec succés")
def recherche_emp_etudiant_livre (window):
    err = ""
    if os.path.exists(fichier) and os.path.getsize(fichier) > 0 and os.path.exists(fichier2) and os.path.getsize(fichier2) > 0 and os.path.exists(fichier3) and os.path.getsize(fichier3) > 0:
        num= window.lineEdit.text()
        ref = window.lineEdit_2.text()
        if len(num)!=8 or num.isdigit()==False :
            err=err+"Verifier le Numéro d'inscription\n"
        else :
            with open(fichier, 'r', newline='') as f:
                reader = csv.DictReader(f)

                f.seek(0)
                rows1 = [row for row in reader if row['Numero_inscription'] == num]
            if not rows1 :
                err += "le numéro d'inscription n'exisite pas\n"
        if not ref.isnumeric():
            err += "Vérifier la référence du livre\n"
        else :
            with open(fichier2 , 'r', newline='') as f:
                reader = csv.DictReader(f)

                f.seek(0)
                rows2 = [row for row in reader if row['reference'] == ref]
            if not rows2 :
                err += "le livre n'exisite pas\n"
        
    else :
        err += "l'un des fichiers est vide ! \n"
    if err:
        show_err(err)
        return
    with open(fichier3, 'r', newline='') as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            print(row.keys())

            if row['Numero_inscription'] == num and row['reference'] == ref:
                rows.append(row)

        if rows:
            fieldnames = ['Numero_inscription','reference','date_emp','date_retour']
            model = CsvTableModelDict(rows, fieldnames)
            window.tableView.setModel(model)
            window.lineEdit.setText("")
            window.lineEdit_2.setText("")
        else:
            window.tableView.setModel(None)
            show_err("Aucun résultat trouvé pour ce niveau de cette section")
def rech_date_ret (window) :
    err = ""
    if os.path.exists(fichier3) and os.path.getsize(fichier3) > 0 :
        date = window.lineEdit.text()
        verif,msg = valid_date2(date)
        if not verif:
            err=err+msg
        else :
            with open(fichier3, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows1 = [row for row in reader if row['date_retour'] == date]
            if not rows1 :
                err += "aucun emprunte avec cette date de retour\n"
        
    else :
        err += "l'un des fichiers est vide ! \n"
    if err:
        show_err(err)
        return
    else :
        fieldnames = ['Numero_inscription','reference','date_emp','date_retour']
        model = CsvTableModelDict(rows1, fieldnames)
        window.tableView.setModel(model)
        window.lineEdit.setText("")

def rech_date_emp (window) :
    err = ""
    if os.path.exists(fichier3) and os.path.getsize(fichier3) > 0 :
        date = window.lineEdit.text()
        verif,msg = valid_date2(date)
        if not verif:
            err=err+msg
        else :
            with open(fichier3, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows1 = [row for row in reader if datetime.datetime.strptime( row['date_emp'] , "%d/%m/%Y")== datetime.datetime.strptime(date, "%d/%m/%Y")]
            if not rows1 :
                err += "aucun emprunte avec cette date d'emprunte \n"
        
    else :
        err += "l'un des fichiers est vide ! \n"
    if err:
        show_err(err)
        return
    fieldnames = ['Numero_inscription','reference','date_emp','date_retour']
    model = CsvTableModelDict(rows1, fieldnames)
    window.tableView.setModel(model)
    window.lineEdit.setText("")
def rech_2date_emp (window) :
    err = ""
    if os.path.exists(fichier3) and os.path.getsize(fichier3) > 0 :
        date1 = window.lineEdit.text()
        date2 = window.lineEdit_2.text()
        verif,msg = valid_2date_emp(date1,date2)
        if not verif:
            err=err+msg
        else :
            date1= datetime.datetime.strptime(date1 , "%d/%m/%Y")
            date2= datetime.datetime.strptime(date2, "%d/%m/%Y")
            with open(fichier3, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows1 = [row for row in reader if date1 <= datetime.datetime.strptime(row['date_emp'] , "%d/%m/%Y")<= date2]
            if not rows1 :
                err += "aucun emprunte entre ces 2 dates \n"   
    else :
        err += "l'un des fichiers est vide ! \n"
    if err:
        show_err(err)
        return

    fieldnames = ['Numero_inscription','reference','date_emp','date_retour']
    model = CsvTableModelDict(rows1, fieldnames)
    window.tableView.setModel(model)
    window.lineEdit.setText("")
    
def rech_2date_ret (window) :
    err = ""
    if os.path.exists(fichier3) and os.path.getsize(fichier3) > 0 :
        date1 = window.lineEdit.text()
        date2 = window.lineEdit_2.text()
        verif,msg = valid_2date_ret(date1,date2)
        if not verif:
            err=err+msg
        else :
            date1= datetime.datetime.strptime(date1 , "%d/%m/%Y")
            date2= datetime.datetime.strptime(date2, "%d/%m/%Y")
            with open(fichier3, 'r', newline='') as f:
                reader = csv.DictReader(f)

                f.seek(0)
                rows1 = [row for row in reader if date1 <= datetime.datetime.strptime(row['date_retour'] , "%d/%m/%Y") <= date2]
            if not rows1 :
                err += "aucun retour d'emprunte entre ces 2 dates\n"
        
    else :
        err += "l'un des fichiers est vide ! \n"
    if err:
        show_err(err)
        return
    fieldnames = ['Numero_inscription','reference','date_emp','date_retour']
    model = CsvTableModelDict(rows1, fieldnames)
    window.tableView.setModel(model)
    window.lineEdit.setText("")


def modif_date_emp(window):
    
    if os.path.exists(fichier3) and os.path.getsize(fichier3) > 0:
        num= window.lineEdit.text()
        ref = window.lineEdit_2.text()
        date_emp1 = window.lineEdit_3.text()
        date_emp2 = window.lineEdit_4.text()
        err = ""
        if len(num)!=8 or num.isdigit()==False :
            err=err+"Verifier le Numéro d'inscription\n"
        if not ref.isnumeric():
            err += "Vérifier la référence du livre\n"
        if not err :
            with open(fichier3, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows1 = [row for row in reader if row['Numero_inscription'] == num and row ['reference']== ref and row['date_emp']== date_emp1]
                if not rows1 :
                    err += "cette emprunte n'exisite pas !"
                else :
                    verif_date,date_err= valid_date_emp(date_emp1,date_emp2,rows1[0]['date_retour'])
                    if not verif_date:
                        err=err+date_err+'\n'
    else :
        err += "l'un des fichiers est vide ! \n"
    if err:
        show_err(err)
        return
    with open(fichier3, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    for row in rows:
        if row['reference'] == ref and row['Numero_inscription']==num  and row['date_emp']== date_emp1:
            row['date_emp'] = date_emp2
            break
    with open(fichier3, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    show_msg("modification avec succés")
def modif_date_ret(window):
    if os.path.exists(fichier3) and os.path.getsize(fichier3) > 0:
        num= window.lineEdit.text()
        ref = window.lineEdit_2.text()
        date_ret1 = window.lineEdit_3.text()
        date_ret2 = window.lineEdit_4.text()
        err = ""
        if len(num)!=8 or num.isdigit()==False :
            err=err+"Verifier le Numéro d'inscription\n"
        if not ref.isnumeric():
            err += "Vérifier la référence du livre\n"
        if not err :
            with open(fichier3, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows1 = [row for row in reader if row['Numero_inscription'] == num and row ['reference']== ref and row['date_retour']== date_ret1]
                if not rows1 :
                    err += "cette emprunte n'exisite pas !"
                else :
                    verif_date,date_err= valid_date_ret(date_ret1,date_ret2,rows1[0]['date_emp'])
                    if not verif_date:
                        err=err+date_err+'\n'
    else :
        err += "l'un des fichiers est vide ! \n"
    if err:
        show_err(err)
        return
    with open(fichier3, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    for row in rows:
        if row['reference'] == ref and row['Numero_inscription']==num  and row['date_retour']== date_ret1:
            row['date_retour'] = date_ret2
            break
    with open(fichier3, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    show_msg("modification avec succés")
def supp_emp(window):
    if os.path.exists(fichier3) and os.path.getsize(fichier3) > 0:
        num= window.lineEdit.text()
        ref = window.lineEdit_2.text()
        date_emp = window.lineEdit_3.text()
        date_ret = window.lineEdit_4.text()
        verif_date,date_err= valid_date1(date_emp,date_ret)
        err = ""
        if len(num)!=8 or num.isdigit()==False :
            err=err+"Verifier le Numéro d'inscription\n"
        if not ref.isnumeric():
            err += "Vérifier la référence du livre\n"
        if not verif_date :
            err += date_err
        if err :
            show_err(err)
            return 
        else :
            with open(fichier3, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['reference'] == ref and row['Numero_inscription']==num  and row['date_retour']== date_ret and row ['date_emp']==date_emp]
                f.seek(0)
                rows1 = [row for row in reader if not(row['reference'] == ref and row['Numero_inscription']==num  and row['date_retour']== date_ret and row ['date_emp']==date_emp)]
            if rows :
                with open(fichier3, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    for row in rows1:
                        writer.writerow(row.values())

                    
                    show_msg("emprunte supprimée avec succès")
            else:
                show_err("l'emprunte n'existe pas")
    else:
        show_err("Le fichier des empruntes est vide")
def ret_emp(window):
    err = ''
    if os.path.exists(fichier3) and os.path.getsize(fichier3) > 0:
        num= window.lineEdit.text()
        ref = window.lineEdit_2.text()
        date_emp = window.lineEdit_3.text()
        date_ret = window.lineEdit_4.text()
        verif_date,date_err= valid_date1(date_emp,date_ret)
        err = ""
        if len(num)!=8 or num.isdigit()==False :
            err=err+"Verifier le Numéro d'inscription\n"
        if not ref.isnumeric():
            err += "Vérifier la référence du livre\n"
        if not verif_date :
            err += date_err
        if err :
            show_err(err)
            return 
        else :
            with open(fichier3, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = []
                for row in reader :
                    if ( row['reference'] == ref and row['Numero_inscription']==num  and datetime.datetime.strptime(row['date_retour'], "%d/%m/%Y")== datetime.datetime.strptime(date_ret, "%d/%m/%Y") and datetime.datetime.strptime( row ['date_emp'], "%d/%m/%Y")==datetime.datetime.strptime(date_emp, "%d/%m/%Y") ):
                        rows.append(row)
            if rows :
                
                with open(fichier2, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['reference'] == ref:
                        row['nombre_exemplaires'] =int(row['nombre_exemplaires'] )+1
                        break
                with open(fichier2, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                
                show_msg("emprunte retournée !")
            else:
                show_err("l'emprunte n'existe pas")
    else:
        show_err("Le fichier des empruntes est vide")
def rech_liv_auteur(window):
    nom = window.lineEdit.text()
    if (nom != ""):
        if os.path.exists(fichier2) and os.path.getsize(fichier2) > 0:
            with open(fichier2, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['auteur'].upper() == nom.upper():
                        rows.append(row)

                if rows:
                    fieldnames = ['reference', 'titre', 'auteur', 'annee','nombre_exemplaires']
                    model = CsvTableModelDict(rows, fieldnames)
                    window.tableView.setModel(model)
                    window.lineEdit.setText("")
                else:
                    window.tableView.setModel(None)
                    show_err("Aucun résultat trouvé pour cet auteur")
        else:
            window.tableView.setModel(None)
            show_err("le fichier des livres est vide ou n'existe pas")
    else:
        window.tableView.setModel(None)
        show_err("Vérifier le nom de l'auteur ")
def recherche_liv_ref(window):
    ref = window.lineEdit.text()
    if (ref != "" and ref.isdigit()):
        if os.path.exists(fichier2) and os.path.getsize(fichier2) > 0:
            with open(fichier2, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['reference'] == ref:
                        rows.append(row)

                if rows:
                    rows = rows
                    fieldnames = ['reference', 'titre', 'auteur', 'annee','nombre_exemplaires']
                    model = CsvTableModelDict(rows, fieldnames)
                    window.tableView.setModel(model)
                    window.lineEdit.setText("")
                else:
                    window.tableView.setModel(None)
                    show_err("Aucun résultat trouvé pour cette réference")
        else:
            window.tableView.setModel(None)
            show_err("le fichier des livres est vide ou n'existe pas")
    else:
        window.tableView.setModel(None)
        show_err("Vérifier la référence ")
def recherche_liv_titre(window):
    titre = window.lineEdit.text()
    if titre != "" :
        if os.path.exists(fichier2) and os.path.getsize(fichier2) > 0:
            with open(fichier2, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['titre'].upper() == titre.upper():
                        rows.append(row)

                if rows:
                    fieldnames = ['reference', 'titre', 'auteur', 'annee','nombre_exemplaires']
                    model = CsvTableModelDict(rows, fieldnames)
                    window.tableView.setModel(model)
                    window.lineEdit.setText("")
                else:
                    window.tableView.setModel(None)
                    show_err("Aucun résultat trouvé pour ce titre")
        else:
            window.tableView.setModel(None)
            show_err("le fichier des livres est vide ou n'existe pas")
    else:
        window.tableView.setModel(None)
        show_err("Vérifier le titre ")
def recherche_liv_annee(window):
    annee = window.lineEdit.text()
    if (annee != "" and annee.isdigit() and 1800<=int(annee)<=2023):
        if os.path.exists(fichier2) and os.path.getsize(fichier2) > 0:
            with open(fichier2, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['annee'] == annee:
                        rows.append(row)

                if rows:
                    fieldnames = ['reference', 'titre', 'auteur', 'annee','nombre_exemplaires']
                    model = CsvTableModelDict(rows, fieldnames)
                    window.tableView.setModel(model)
                    window.lineEdit.setText("")
                else:
                    window.tableView.setModel(None)
                    show_err("Aucun résultat trouvé pour cette année")
        else:
            window.tableView.setModel(None)
            show_err("le fichier des livres est vide ou n'existe pas")
    else:
        window.tableView.setModel(None)
        show_err("Vérifier l'année ")


def tri(window_show_contenu):
    if os.path.exists(fichier2) and os.path.getsize(fichier2) > 0:
        model = QStandardItemModel()
        model.clear()
        df = pd.read_csv('livres.csv')
        df_sorted = df.sort_values(by='titre')  # Tri des livres par ordre alphabétique
        model.setHorizontalHeaderLabels(header2) 
        for row in range(df_sorted.shape[0]):
            model.insertRow(row)
            for col in range(df_sorted.shape[1]):
                item = QStandardItem(str(df_sorted.iloc[row, col]))
                model.setItem(row, col, item)
        window_show_contenu.tableView.setModel(model)
    else:
        show_err("Le fichier des livres est vide")
