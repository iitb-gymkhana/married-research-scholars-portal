def gsheets_automation():
    import imaplib
    import email
    import os
    import glob
    import gspread
    from django.conf import settings
    from google.oauth2.service_account import Credentials
    from google.auth.transport.requests import AuthorizedSession
    from django.template.loader import get_template
    from django.shortcuts import render

    credentials_file = settings.GOOGLE_APPLICATION_CREDENTIALS_PATH
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = Credentials.from_service_account_file(credentials_file, scopes=scopes)
    gc = gspread.Client(auth=credentials)
    gc.session = AuthorizedSession(credentials)
    sheet = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1rMawoIJLg01CsgkRN1pL5ap_EGyTmpe6LSGJkHrLZRQ/edit#gid=0")
    worksheet = sheet.get_worksheet(0)
    # values_list = worksheet.row_values(1)
    # var = sheet_links.cell(1, 2).value
    lists = worksheet.get_all_values()
    list_of_dicts = worksheet.get_all_records()
    template_src = "hcu_template.html"
    template = get_template(template_src)
    # list_of_dicts = list_of_dicts .flatten()
    dictn = {'list_of_dicts': list_of_dicts}
    html = template.render(dictn)
    html_file = open("hcu.html", "w")
    html_file.write(html)
    html_file.close()
    return list_of_dicts
    # sheet.sheets[1].to_csv('Spam.csv', encoding='utf-8', dialect='excel')

    # return render(None, template_src, list_of_dicts)
