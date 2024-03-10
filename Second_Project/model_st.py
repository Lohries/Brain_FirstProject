from deepface import DeepFace
import cv2 as cv
import os 


def data_base_analyze(data):
    directory = "img"
    lista2 = []
    for i in enumerate(os.listdir(directory)):
        
        results = DeepFace.analyze(f"img/img{i+1}")
        if results:
            print("Age: ", results[0]["age"])
            print("Gender: ", results[0]["gender"])
            print("Emotion: ", results[0]["dominant_emotion"])
            print("Race: ", results[0]["dominant_race"])
            points = 0
            if results[0]["dominant_emotion"] == data[0]:
                points += 1
            elif results[0]["age"] == data[1]:
                points += 1
            elif results[0]["gender"] == data[2]:
                points += 1
            elif results[0]["dominant_race"] == data[3]:
                points += 1
            
            lista2.append(points)







#def analyze_submit():
    #pass

