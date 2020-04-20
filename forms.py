
class RunForm():
    def __init__(self,request):
        self.brr = request.values.get('Behavioral Risk Reduction')
        self.pie = request.values.get('Potential Isolation Effectiveness')
        self.selt = request.values.get('selectedTime')
    
    def parsed(self):
        return {
            'Behavioral Risk Reduction': self.brr,
            'Potential Isolation Effectiveness': self.pie,
            'selected_time': self.selt
        }


class SaveRunForm():
    def __init__(self,request):
        # self.id = request.values.get('runId')
        self.name = request.values.get('runName')
        self.run = RunForm(request)
        
    def parsed(self):
        # parsed_form = { 'id': self.id, 'name' : self.name }
        parsed_form = {'name' : self.name }
        parsed_form.update(self.run.parsed())
        return parsed_form


# class UpdateRunForm():
#     def __init__(self,request):
#         self.id = request.values.get('runId')
#         self.run = SaveRunForm(request)
    
#     def parsed(self):
#         parsed_form = {'id': self.id}
#         parsed_form.update(self.run.parsed())
#         return parsed_form

