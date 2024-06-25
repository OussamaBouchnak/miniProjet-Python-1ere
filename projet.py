from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
import icon_rc
import functions

app = QApplication([])


window = loadUi("miniprojet.ui")
window.show()
window.tabWidget.tabBar().setVisible(False)
window.acceuil.setEnabled(False)
window.gest_livre.setEnabled(False)
window.enreg_recup.setEnabled(False)
window.gest_emp.setEnabled(False)
window.tabWidget.setCurrentIndex(0)
window.quitter.clicked.connect(lambda: window.close())
window.entrer.clicked.connect(lambda: functions.passwd(window))
window.acceuil.clicked.connect(lambda: window.tabWidget.setCurrentIndex(0))
window.gest_livre.clicked.connect(lambda: window.tabWidget.setCurrentIndex(1))
window.enreg_recup.clicked.connect(lambda: window.tabWidget.setCurrentIndex(2))
window.gest_emp.clicked.connect(lambda: window.tabWidget.setCurrentIndex(3))

#*******************************ajout etudiant*****************************

win_add_student=loadUi("ajoutEtud.ui")

window.ajouter_etud.clicked.connect(win_add_student.show)

win_add_student.ajout.clicked.connect(lambda : functions.add_student(win_add_student))

win_add_student.annuler.clicked.connect(lambda : win_add_student.close())

#*******************************supp etudiant donné*****************************

window_Supp_etud=loadUi("suppEtud.ui")

window.supp_etud.clicked.connect(window_Supp_etud.show)

window_Supp_etud.supprimer.clicked.connect(lambda : functions.delete(window_Supp_etud))
window_Supp_etud.pushButton.clicked.connect(lambda : window_Supp_etud.close())


#*******************************supp section*****************************

window_Supp_sec=loadUi("suppSec.ui")

window.supp_sec.clicked.connect(window_Supp_sec.show)

window_Supp_sec.pushButton.clicked.connect(lambda: functions.supprimer_section(window_Supp_sec))
window_Supp_sec.pushButton_2.clicked.connect(lambda:window_Supp_sec.close())

#*******************************supp niveau*****************************


window_Supp_niv=loadUi("suppNiv.ui")

window.supp_niv.clicked.connect(window_Supp_niv.show)

window_Supp_niv.pushButton.clicked.connect(lambda: functions.supprimer_niveau(window_Supp_niv))
window_Supp_niv.pushButton_2.clicked.connect(lambda: window_Supp_niv.close())


#*******************************supp niveau section*****************************


window_Supp_sec_niv=loadUi("suppSecNiv.ui")

window.supp_sec_niv.clicked.connect(window_Supp_sec_niv.show)

window_Supp_sec_niv.pushButton.clicked.connect(lambda: functions.supprimer_section_niveau(window_Supp_sec_niv))
window_Supp_sec_niv.pushButton_2.clicked.connect(lambda: window_Supp_sec_niv.closse())

#*******************************affichage etudiants*****************************
window_affichage = loadUi("affEtud.ui")

window.aff_etud.clicked.connect(window_affichage.show)

window_affichage.pushButton.clicked.connect(lambda: functions.affichage(window_affichage))

window_affichage.pushButton_2.clicked.connect(lambda: functions.annuler(window_affichage))
#*******************************affichage livres*****************************
window_affichage_livre = loadUi("affLiv.ui")

window.aff_liv.clicked.connect(window_affichage_livre.show)

window_affichage_livre.pushButton.clicked.connect(lambda: functions.affichage_livre(window_affichage_livre))

window_affichage_livre.pushButton_2.clicked.connect(lambda: functions.annuler(window_affichage_livre))
#*******************************affichage emprunt *****************************
window_affichage_emp = loadUi("affEmp.ui")

window.aff_emp.clicked.connect(window_affichage_emp.show)

window_affichage_emp.pushButton.clicked.connect(lambda: functions.affichage1(window_affichage_emp))

window_affichage_emp.pushButton_2.clicked.connect(lambda: functions.annuler(window_affichage_emp))

#*******************************recherche etudiant par niveau  *****************************

window_rech_niv=loadUi("rechNiv.ui")

window.rech_niv.clicked.connect(window_rech_niv.show)

window_rech_niv.pushButton.clicked.connect(lambda: functions.recherche_niv(window_rech_niv))

window_rech_niv.pushButton_2.clicked.connect(lambda: functions.annuler(window_rech_niv))

#*******************************recherche etudiant par niveau  *****************************

window_rech_sec=loadUi("rechSec.ui")

window.rech_sec.clicked.connect(window_rech_sec.show)

window_rech_sec.pushButton.clicked.connect(lambda: functions.recherche_sec(window_rech_sec))

window_rech_sec.pushButton_2.clicked.connect(lambda: functions.annuler(window_rech_sec))

#*******************************recherche etudiant par section  *****************************

window_rech_niv=loadUi("rechNiv.ui")

window.rech_niv.clicked.connect(window_rech_niv.show)

window_rech_niv.pushButton.clicked.connect(lambda: functions.recherche_niv(window_rech_niv))

window_rech_niv.pushButton_2.clicked.connect(lambda: functions.annuler(window_rech_niv))

#*******************************recherche etudiant par section et niveau *****************************

window_rech_sec_niv=loadUi("rechSecNiv.ui")

window.rech_sec_niv.clicked.connect(window_rech_sec_niv.show)

window_rech_sec_niv.pushButton.clicked.connect(lambda: functions.recherche_sec_niv(window_rech_sec_niv))

window_rech_sec_niv.pushButton_2.clicked.connect(lambda: functions.annuler(window_rech_sec_niv))

#*******************************recherche etudiant par numero d'inscription *****************************

window_rech_num=loadUi("rechNumInsc.ui")

window.rech_num_insc.clicked.connect(window_rech_num.show)

window_rech_num.pushButton.clicked.connect(lambda: functions.recherche_num(window_rech_num))

window_rech_num.pushButton_2.clicked.connect(lambda: functions.annuler(window_rech_num))
#*******************************ajout livre *****************************

window_ajout_livre=loadUi("ajouter_livre.ui")

window.ajout_livre.clicked.connect(window_ajout_livre.show)

window_ajout_livre.pushButton.clicked.connect(lambda: functions.ajout_livre(window_ajout_livre))

window_ajout_livre.pushButton_2.clicked.connect(lambda: functions.annuler1(window_ajout_livre))
#*******************************modifier tel étudiant  *****************************

window_modif_tel=loadUi("modifTel.ui")

window.modif_tel.clicked.connect(window_modif_tel.show)

window_modif_tel.pushButton.clicked.connect(lambda: functions.modifier_telephone(window_modif_tel))

window_modif_tel.pushButton_2.clicked.connect(lambda: window_modif_tel.close())
#*******************************modifier adresse étudiant  *****************************

window_modif_adresse=loadUi("modifAdresse.ui")

window.modif_adresse.clicked.connect(window_modif_adresse.show)

window_modif_adresse.pushButton.clicked.connect(lambda: functions.modifier_adresse(window_modif_adresse))

window_modif_adresse.pushButton_2.clicked.connect(lambda: window_modif_adresse.close())
#*******************************modifier email étudiant  *****************************

window_modif_mail=loadUi("modifMail.ui")

window.modif_mail.clicked.connect(window_modif_mail.show)

window_modif_mail.pushButton.clicked.connect(lambda: functions.modifier_mail(window_modif_mail))

window_modif_mail.pushButton_2.clicked.connect(lambda: window_modif_mail.close())
#*******************************ajout emprunt *****************************

window_ajout_emp=loadUi("ajoutEmp.ui")

window.ajout_emp.clicked.connect(window_ajout_emp.show)

window_ajout_emp.pushButton.clicked.connect(lambda: functions.ajout_emp(window_ajout_emp))

window_ajout_emp.pushButton_2.clicked.connect(lambda: functions.annuler1(window_ajout_emp))
#*******************************rech emprunte par livre etudiant *****************************

window_rech_liv_etud=loadUi("rechLivEtud.ui")

window.rech_liv_etud.clicked.connect(window_rech_liv_etud.show)

window_rech_liv_etud.pushButton.clicked.connect(lambda: functions.recherche_emp_etudiant_livre(window_rech_liv_etud))

window_rech_liv_etud.pushButton_2.clicked.connect(lambda: window_rech_liv_etud.close())
#*******************************recherche emprunt retourné a une date donné *****************************

window_rech_date_ret = loadUi("rechLivRDate.ui")

window.rech_date_ret.clicked.connect(window_rech_date_ret.show)

window_rech_date_ret.pushButton.clicked.connect(lambda: functions.rech_date_ret(window_rech_date_ret))

window_rech_date_ret.pushButton_2.clicked.connect(lambda: window_rech_date_ret.close())
#*******************************recherche empruntés a une date donné *****************************

window_rech_date_emp = loadUi("rechLivEDate.ui")

window.rech_date_emp.clicked.connect(window_rech_date_emp.show)

window_rech_date_emp.pushButton.clicked.connect(lambda: functions.rech_date_emp(window_rech_date_emp))

window_rech_date_emp.pushButton_2.clicked.connect(lambda: window_rech_date_emp.close())
#*******************************recherche livres empruntés entre deux dates données *****************************

window_rech_2date_emp = loadUi("rechLivE2Date.ui")

window.rech_2date_emp.clicked.connect(window_rech_2date_emp.show)

window_rech_2date_emp.pushButton.clicked.connect(lambda: functions.rech_2date_emp(window_rech_2date_emp))

window_rech_2date_emp.pushButton_2.clicked.connect(lambda: window_rech_2date_emp.close())
#*******************************recherche livres retournés entre deux dates données  *****************************

window_rech_2date_ret = loadUi("rechLivR2Date.ui")

window.rech_2date_ret.clicked.connect(window_rech_2date_ret.show)

window_rech_2date_ret.pushButton.clicked.connect(lambda: functions.rech_2date_ret(window_rech_2date_ret))

window_rech_2date_ret.pushButton_2.clicked.connect(lambda: window_rech_2date_ret.close())
#*******************************modificaton de la date de retour d'une emprunte *****************************

window_modif_date_ret = loadUi("modifDateRet.ui")

window.modif_date_ret.clicked.connect(window_modif_date_ret.show)

window_modif_date_ret.pushButton.clicked.connect(lambda: functions.modif_date_ret(window_modif_date_ret))

window_modif_date_ret.pushButton_2.clicked.connect(lambda: window_modif_date_ret.close())
#*******************************modificaton de la date d'emprunte *****************************

window_modif_date_emp = loadUi("modifDateEmp.ui")

window.modif_date_emp.clicked.connect(window_modif_date_emp.show)

window_modif_date_emp.pushButton.clicked.connect(lambda: functions.modif_date_emp(window_modif_date_emp))

window_modif_date_emp.pushButton_2.clicked.connect(lambda: window_modif_date_emp.close())
#*******************************supprimer emprunte *****************************

window_supp_emp = loadUi("suppEmp.ui")

window.supp_emp.clicked.connect(window_supp_emp.show)

window_supp_emp.pushButton.clicked.connect(lambda: functions.supp_emp(window_supp_emp))

window_supp_emp.pushButton_2.clicked.connect(lambda: window_supp_emp.close())
#*******************************retour emprunte *****************************

window_ret_emp = loadUi("retourEmp.ui")

window.retour_emp.clicked.connect(window_ret_emp.show)

window_ret_emp.pushButton.clicked.connect(lambda: functions.ret_emp(window_ret_emp))

window_ret_emp.pushButton_2.clicked.connect(lambda: window_ret_emp.close())
#*******************************recherche livre d'un auteur donné  *****************************

window_rech_aut=loadUi("rechLivAut.ui")

window.rech_aut.clicked.connect(window_rech_aut.show)

window_rech_aut.pushButton.clicked.connect(lambda: functions.rech_liv_auteur(window_rech_aut))

window_rech_aut.pushButton_2.clicked.connect(lambda: functions.annuler(window_rech_aut))

#*******************************recherche livres par reference  *****************************

window_rech_ref=loadUi("rechLivRef.ui")

window.rech_ref.clicked.connect(window_rech_ref.show)

window_rech_ref.pushButton.clicked.connect(lambda: functions.recherche_liv_ref(window_rech_ref))

window_rech_ref.pushButton_2.clicked.connect(lambda: functions.annuler(window_rech_ref))
#*******************************recherche livres par annee edition  *****************************

window_rech_annee=loadUi("rechLivAnnee.ui")

window.rech_annee.clicked.connect(window_rech_annee.show)

window_rech_annee.pushButton.clicked.connect(lambda: functions.recherche_liv_annee(window_rech_annee))

window_rech_annee.pushButton_2.clicked.connect(lambda: functions.annuler(window_rech_annee))
#*******************************recherche livres par titre  *****************************

window_rech_titre=loadUi("rechLivTitre.ui")

window.rech_titre.clicked.connect(window_rech_titre.show)

window_rech_titre.pushButton.clicked.connect(lambda: functions.recherche_liv_titre(window_rech_titre))

window_rech_titre.pushButton_2.clicked.connect(lambda: functions.annuler(window_rech_titre))
#*******************************supprimer un livre   *****************************

window_supp_liv=loadUi("suppLivre.ui")

window.supp_liv.clicked.connect(window_supp_liv.show)

window_supp_liv.pushButton.clicked.connect(lambda: functions.supprimer_livre(window_supp_liv))

window_supp_liv.pushButton_2.clicked.connect(lambda: functions.annuler2(window_supp_liv))
#*******************************aff livre  par ordre alphabétique*****************************

window_tri=loadUi("afftri.ui")

window.tri.clicked.connect(window_tri.show)

window_tri.pushButton.clicked.connect(lambda: functions.tri(window_tri))

window_tri.pushButton_2.clicked.connect(lambda: functions.annuler(window_tri))


app.exec()