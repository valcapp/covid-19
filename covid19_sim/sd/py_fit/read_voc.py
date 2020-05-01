import os
# dir_name = os.path.dirname(__file__)
dir_name = os.getcwd()
voc_name = next((name for name in os.listdir( dir_name ) if name.split('.')[-1]=='voc' in name), None)

lines = open(voc_name, "r").readlines()
# lines = [line.strip() for line in lines]

params={}
for line in lines:
    if line[0]!=':':
        terms = line.split('<=')
        mid_terms = terms[1].split('=')
        param_name = mid_terms[0].strip()
        new_param = {
            param_name:{
                'min':float(terms[0].strip()),
                'max': float(terms[2].strip()),
            }
        }
        if len(mid_terms)>1:
            new_param[param_name].update({'value':float(mid_terms[1].strip())})
        params.update(new_param)