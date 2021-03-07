import re
class PRParser:
    def __init__(self, text):
        """ 
            PRParser(<string>)
            Returns [
            name,
            event_type,
            event_date,
            event_year,
            pr_res_place,
            pr_age,
            pr_mil_company_regiment,
            pr_mil_regiment,
            pr_mil_battalion,
            pr_bir_date,
            pr_bir_place
        ]
        """
        self.text = text
        self.parse()
    
    def parse(self):
        [name,
        event_type,
        event_date,
        event_year,
        pr_res_place,
        pr_age,
        pr_mil_company_regiment,
        pr_mil_regiment,
        pr_mil_battalion,
        pr_bir_date,
        pr_bir_place] = [None]*11
        
        try:
            name = re.findall(r'"labelId" : "PR_NAME",[\n\t\s]+"text" : "([\w\s,\'\"\-]+)"', self.text)[0]
        except:
            pass
        try:
            event_type =  re.findall(r'"labelId" : "EVENT_TYPE",[\n\t\s]+"text" : "([\w\s,]+)"', self.text)[0]
        except:
            pass
        try:
            event_date = re.findall(r'"labelId" : "EVENT_DATE",[\n\t\s]+"text" : "([\w\s]+)"', self.text)[0]
        except:
            pass

        try:
            event_year = re.findall(r'"labelId" : "EVENT_YEAR",[\n\t\s]+"text" : "([\w\s]+)"', self.text)[0]
        except:
            pass

        try:
            pr_res_place = re.findall(r'"labelId" : "PR_RES_PLACE",[\n\t\s]+"text" : "([\w\s,\/]+)"', self.text)[0]
        except:
            pass
        
        try:
            pr_age = re.findall(r'"labelId" : "PR_AGE",[\n\t\s]+"text" : "([\w\s]+)"', self.text)[0]
        except:
            pass

        try:
            pr_mil_company_regiment = re.findall(r'"labelId" : "PR_MIL_COMPANY_REGIMENT",[\n\t\s]+"text" : "([\w\s,\/]+)"', self.text)[0]
        except:
            pass
        
        try:
            pr_mil_regiment = re.findall(r'"labelId" : "PR_MIL_REGIMENT",[\n\t\s]+"text" : "([\w\s,\/]+)"', self.text)[0]
        except:
            pass

        try:
            pr_mil_battalion = re.findall(r'"labelId" : "PR_MIL_BATTALION",[\n\t\s]+"text" : "([\w\s,\/]+)"', self.text)[0]
        except:
            pass

        try:
            pr_bir_date = re.findall(r'"labelId" : "PR_BIR_YEAR_EST",[\n\t\s]+"text" : "([\w\s]+)"', self.text)[0]
        except:
            pass

        try:
            pr_bir_place= re.findall(r'"labelId" : "PR_BIR_PLACE",[\n\t\s]+"text" : "([\w\s,]+)"', self.text)[0]
        except:
            pass
        
        self.data = [
            name,
            event_type,
            event_date,
            event_year,
            pr_res_place,
            pr_age,
            pr_mil_company_regiment,
            pr_mil_regiment,
            pr_mil_battalion,
            pr_bir_date,
            pr_bir_place
        ]
    
    def get_data(self):
        return self.data
    
    def clear_data(self):
        del self.data
