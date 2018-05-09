
import Hood_ObjectDetectModule as o

myTraining="training.xml"

myTesting ="testing.xml"

faces_folder ="E:\\700_Tutorials\\dlib\\examples\\faces"

myDetector="myDetector.svm"
myHOGDetector="myHOGDetector.svm"

o.train_object_detector(faces_folder,myTraining,myTesting,myDetector,myHOGDetector)