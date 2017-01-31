def sme_v5_and_contact_v3_to_finance_application_v3_translator(sme, sme_contact):
    applicant = {'first_name':sme_contact.get('applicant_first_name', ''),
                 'phone_number': sme_contact.get('phone_number'),
                 'surname': sme_contact.get('applicant_surname', '')
                 }
    requesting_entity = {"name":sme_contact['sme_name']}
    for field in ('legal_status', 'months_revenue', 'trade_credit', 'revenue', 'sic_code'):
        if field in sme:
            requesting_entity[field] = sme[field]
    finance_need = {}
    for field in ('purpose','finance_term_length', 'date_finance_requested', 'requested_amount'):
        if field in sme:
            finance_need[field] = sme[field]

    return {
            'applicant': applicant,
            'requesting_entity': requesting_entity,
            'finance_need': finance_need
           }

