from db import db
import json

def try_load(value):
    if type(value) is str:
        return json.loads(value)
    else:
        return None

class Run(db.Model):
    __tablename__ = 'runs'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    params = db.Column(db.Text)
    results = db.Column(db.Text)
    selected_time = db.Column(db.Integer)
    # params_id = db.relationship('Params',backref='run',uselist=False)
    # results_id = db.relationship('Results',backref='run',uselist=False)

    # initialization
    def __init__(self,name,params,results,selected_time):
        self.edit(name,params,results,selected_time)
        # self.name = name
        # self.params = params
        # self.results = results
        # self.selected_time = selected_time

        # print('In Run dbModel: input: ',selected_time)
        # print('output: ',self.selected_time)
    
    def edit(self,name,params,results,selected_time):
        self.name = name
        self.params = params
        self.results = results
        self.selected_time = selected_time
    
    # db operations
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self,name,params,results,selected_time):
        self.edit(name,params,results,selected_time)
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # output/ representation
    def json(self):
        return {
            'id':self.id,
            'name' : self.name,
            'params' : try_load(self.params),
            'results' : try_load(self.results),
            'selected_time' : self.selected_time
        }

    def __repr__(self):
        return json.dumps(self.json())


# class Params(db.Model):
#     __tablename__ = 'params'
#     id = db.Column(db.Integer,primary_key=True)
#     behavioral_risk_reduction = db.Column(db.Float)
#     potential_isolation_effectiveness = db.Column(db.Float)
#     run_id = db.Column(db.Unicode,db.ForeignKey('runs.id'))

#     def __init__(self,name,brr,pie,run_id):
#         self.name = name
#         self.behavioral_risk_reduction = brr
#         self.potential_isolation_effectiveness = pie
#         self.run_id = run_id

#     def __repr__(self):
#         repres = {
#             'Behavioral Risk Reduction':self.behavioral_risk_reduction,
#             'Potential Isolation Effectiveness':self.potential_isolation_effectiveness
#         }
#         return json.dumps(repres)


# class Results(db.Model):
#     __tablename__ = 'results'
#     id = db.Column(db.Unicode,primary_key=True)
#     json_data = db.Column(db.Unicode)
#     run_id = db.Column(db.Unicode,db.ForeignKey('runs.id'))
#     stamp_id = db.relationship('Stamp',backref='results',lazy='dynamic')
#     # stamp_id = db.Column(db.Unicode, db.ForeignKey('stamps.id'))

#     def __init__(self,id,data):
#         self.id = id
#         self.json_data = data
    
#     def __repr__(self):
#         return self.json_data


# class Stamp(db.Model):
#     __tablename__ = 'steps'
#     id = db.Column(db.Unicode,primary_key=True)
#     time = db.Column(db.Float)
#     susceptible = db.Column(db.Float)
#     exposed = db.Column(db.Float)
#     infected = db.Column(db.Float)
#     recovered = db.Column(db.Float)
#     deaths = db.Column(db.Float)
#     results_id = db.Column(db.Unicode,db.ForeignKey('results.id'))

#     def __init__(self,step,time,s,e,i,r,d,results_id):
#         self.id = step
#         self.time = time
#         self.susceptible = s
#         self.exposed = e
#         self.infected = i
#         self.recovered = r
#         self.deaths = d
#         self.results_id = results_id

#     def __repr__(self):
#         repres = {
#             'time' : self.time,
#             'susceptible' : self.susceptible,
#             'exposed' : self.exposed,
#             'infected' : self.infected,
#             'recovered' : self.recovered,
#             'deaths' : self.deaths,
#             'results_id' : self.results_id
#         }
#         return json.dumps(repres)

