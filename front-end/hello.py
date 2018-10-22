from flask import Flask,request
import sys
import json
from flask_cors import CORS

from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import pandas as pd
import numpy as np
import json as jsn

symptoms = ["Upper abdominal pain","Lower abdominal pain","Abscess (Collection of pus)","Alcohol abuse","Anxiety (Nervousness)","Arm ache or pain","Back ache or pain","Bleeding tendency","Blood in vomit","Bloody diarrhea","Pain or soreness of breast","Calf pain","Chest pressure","Chills","Change in behavior","Constipation","Cough","Dark stools","Depressed","Diarrhea","Dizziness","Double vision (Diplopia)","Ear pressure","Pain in the ear","Elbow ache or pain","Eye pain (Irritation)","Facial pain","Fainting","Fever","Fever in the returning traveler","Fever of unknown origin","Flank pain","Frequent urination (Frequency)","Foot pain","Cranky, crying, fussy, irritable child","Groin pain","Delusions or hallucinations","Hand, finger ache or pain","Head injury","Headache","Heel pain","Heat illness","Hip pain","Hives","Hoarse voice","Hypothermia (Low temperature)","Incontinence (leaking urine)","Insect sting","Insomnia (Trouble sleeping)","Skin itching","Joint pain","Kidney pain (Flank pain)","Knee pain","Laceration","Leg ache or pain","Swelling of both legs","Lethargy (Sluggishness)","Mouth pain","Muscle pain","Nail Injury","Nasal bleeding","Nasal injury","Nausea","Neck ache or pain","Neck swelling","Numbness","Obesity","Overdose","Painful urination","Heart pulsations and palpitations","Pelvic pain","Penile discharge","Penis pain","Poisoning","Pregnancy problem","Psychiatric problem","Puncture wound","Rash","Rectal pain","Rectal swelling","Scrotal pain","Scrotal swelling","Seizure","Shortness of breath","Shoulder ache or pain","Sinus pain and pressure","Skin trauma","Snake bite","Sore throat","Speech problem","Spider bite","Substance abuse (Drug abuse)","Suicidal tendencies","Swallowing problem (Dysphagia)","Swelling","Toe pain","Tooth pain","Trauma","Traveler's diarrhea","Unsteady gait (Trouble walking)","Vaginal bleeding","Vaginal bleeding after menopause","Vaginal bleeding during pregnancy","Vaginal discharge","Vaginal itching","Vaginal pain","Vertigo (Room spinning)","Visual problems","Vomiting","General weakness","Weakness (Muscle localized)","Tired","Wrist pain","Throat pain","Tremors","Weight loss, unexplained","Tongue swelling","Inconsolable baby","Wheezing (Noisy breathing)","Swollen lymph nodes (Large lymph nodes)","Failure to thrive","Behavioral problem","Itchy rash (Pruritic rash)","Headache after trauma","Learning difficulties","Blood in urine (Hematuria)","Urinary retention (Inability to urinate)","Liver failure (Cirrhosis)","Choking","Painful rash","Ingestion","Melena (Black stools from blood)","Vomiting coffee ground material","Ringing in ears (Tinnitus)","Mouth ulcers","Mouth swelling","Eye redness","Sneezing","Bleeding gums","Loss of balance","Bleeding in brain","Cyanosis (Blue skin coloration)","Muscle spasm","Drooling","Abdominal swelling (Stomach swelling)","Skin growths","Hand numbness (paresthesias)","Ankle pain","Hemoptysis (Coughing blood)","Jaundice (Yellowing skin)","Night sweats","Flatulence (Passing gas)","Blister (Pocket of fluid)","Hair loss (Baldness)","Jaw pain","Impotence","Heart murmur (Abnormal heart sound)","Pustule (Collection of pus)","Skin pain","Hot skin","Skin swelling","Lip swelling","Eye swelling","Foot swelling","Visual flashing lights","Eye floaters","Amenorrhea (No menstruation)","Blurry vision","Painful gums","Swollen gums","Low blood sugar","Low blood pressure","Darkening of the skin (Hyperpigmentation)","Low heart rate","Foot itching","Hot flashes","Infertility (Female)","Increased facial hair","Arm swelling","Calf swelling","Ear swelling","Wrist swelling","Maroon stools","Arm cut (laceration)","Hand cut (laceration)","Leg cut (laceration)","Foot cut (laceration)","Arm itching","Hand redness","Foot redness","Arm redness","Leg redness","Hand itching","Leg itching","Steatorrhea (Excess fat in stool)","Upper leg pain","Armpit pain","Sweating","Nasal congestion","Joint stiffness","Skin sores","Chest burning","Memory loss","Arm numbness (paresthesias)","Leg numbness (paresthesias)","Foot numbness (paresthesias)","Face numbness (paresthesias)","Dementia","Facial droop (weakness)","Limping in a child","Increased thirst","Increased urination (polyuria)","Shin pain","Stings","Sleep disorders","Drooping eyelid (Ptosis)","Snoring","Dry skin","Itchy eyes","Elbow swelling","Chest pain","Skin infection","Stomach and abdominal pain","Anger","Hurts to breathe","Difficulty breathing","Pulling at ears","Skin bumps","Congestion in chest or lungs","Discharge from ear","Low back ache or pain","Unusual color or odor of urine","Penis inflammation or swelling","Excessive appetite","Retaining fluid","Lump or mass of breast","Neck stiffness or tightness","Agitated","Confusion","Headache and weakness","Confusion and headache","Nipple discharge","Shoulder stiffness or tightness","Arm stiffness or tightness","High blood pressure","High blood sugar"]

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "This is the main page"


@app.route("/test", methods = ['POST'])
def test():
#    if request.method == 'POST':
#        json_data = json.loads(str(request.body, encoding='utf-8'))
#        print(json_data, file = sys.stderr)
    print(request.data, file=sys.stderr)
    #theJson = json.loads(request.data)
    #print("SESSION: " + theJson.session, file=sys.stderr)
        
    with open('test.json') as f:
        data = json.load(f)
        
    
    
    return json.dumps(data)
    
@app.route("/webSubmit", methods = ['POST'])
def submitWeb():
#    if request.method == 'POST':
#        json_data = json.loads(str(request.body, encoding='utf-8'))
#        print(json_data, file = sys.stderr)
    #print(request.data, file=sys.stderr)
    jsonStr = request.data.decode('utf-8')
    jsonObj = json.loads(jsonStr)
    print("=====RECEIVED SYMPTOMS=====", file=sys.stderr)
    
    lst = []
    for v in jsonObj:
        print(v, file=sys.stderr)
        lst.append(v)
     #theJson = json.loads(request.data)
    #print("SESSION: " + theJson.session, file=sys.stderr)
    theThingy = symptomsToOneHot(lst)
    #with open('onehot.json', 'w') as outfile:
     #   json.dump(theThingy, outfile)
    #Call machine learning
    print(theThingy, file=sys.stderr)
    
    theRet = doItAll(theThingy)
    #print("THIS THING RIGHT HERE" + str(theRet), file=sys.stderr)
    #print("Length = " + str(len(theRet)), file=sys.stderr)
    #Return machine learning
    #with open('website.json') as f:
     #   data = json.load(f)
    #print("SENDING: " + str(json.dumps(data)), file = sys.stderr)
    
    foundDiseases = {}
    diseaseArr = []
    
    for abc in theRet:
        tempDict = {}
        tempDict["label"] = str(abc[0])
        tempDict["value"] = str(abc[1])
        diseaseArr.append(tempDict)
    foundDiseases["diseases"] = diseaseArr
    
    
    return json.dumps(foundDiseases)

def symptomsToOneHot(arr):
    print("LENGTH: " + str(len(symptoms)) , file=sys.stderr)
    arr3 = []
    for symp in symptoms:
        found = False
        for given in arr:
            if given == symp:
                found = True
        if found:
            arr3.append(1)
        else:
            arr3.append(0)
    #twoJson = json.dumps(oneJson)
    #print(json.dumps(oneJson), file=sys.stderr)
    return arr3







def prep_data(path):
    data = pd.read_csv(path ,encoding='utf-8', engine='python')
    diaData = data.values[:, 0]
    symData = data.values[:, 2:]
    diaData = diaData.astype('int')
    diaName = data.values[:, 1]
    return symData, diaData, diaName


def justFitIt(logisticReg, symptom_data, diagnosis_data):
    logisticReg.fit(symptom_data, diagnosis_data)


def justDoIt(logReg, predData):
    ##predData should be a 1d array
    result_data = logReg.predict_proba([predData])
    return result_data


def cleanData(diagnosis_names, probability_values):
    combined = np.vstack((diagnosis_names, probability_values)).T
    combined = combined[combined[:, 1].argsort()]
    combined = np.flip(combined, axis=0)
    return combined[:5]

def doItAll(prediction_data):
    data_path = "/home/ec2-user/symptomizer/front-end/sym_dis_frame_finished.csv"
    lr = LogisticRegression(solver='newton-cg', multi_class='multinomial')
    symData, diaData, diaName = prep_data(data_path)
    justFitIt(lr, symData, diaData)
    resData = justDoIt(lr, prediction_data)
    finalData = cleanData(diaName, resData)
    return finalData
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
