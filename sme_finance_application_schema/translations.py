def sme_v5_and_contact_v3_to_finance_application_v3_translator(sme, sme_contact):
    applicant = {'first_name':sme_contact.get('applicant_first_name', ''),
                 'surname': sme_contact.get('surname', '')
                 }
    requesting_entity = {"name":sme_contact['sme_name']}
    finance_need = {}
    if sme.get('legal_status'):
        requesting_entity['legal_status'] = sme['legal_status']

    return {
            'applicant': applicant,
            'requesting_entity': requesting_entity,
            'finance_need': finance_need
           }

