#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 04:59:39 2020

@author: Haitham Essam 
"""


from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
styles = getSampleStyleSheet()

def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    #report_table = Table(data=paragraph)
    
    
    #table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
    #report_table = Table(data=paragraph, style=table_style, hAlign="LEFT")
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1,20)

    report.build([report_title, empty_line, report_info, empty_line])
    #report.build([report_title, report_table])