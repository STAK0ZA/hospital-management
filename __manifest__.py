{
    'name': 'Hospital App',
    'author': 'Stakoza',
    'version': '17.0.0.1.0',
    'depends': ['base','mail','product'],
    'data': [
        "security/ir.model.access.csv",
        "data/load_data.xml",
        "data/patient.tags.csv",
        "wizard/appointment_cancel.xml",
        "views/main_menu.xml",
        "views/femal_patient.xml",
        "views/patient_actionsandmenu.xml",
        "views/apppointment_page.xml",
        "views/patient_tags.xml",

    ],
    'application': True,
}
