
import Hood_ObjectDetectModule as o

myTraining="bibdataset_reduced_more.xml"

myTesting ="bibdataset_reduced_more.xml"

#faces_folder ="E:\\700_Tutorials\\dlib\\examples\\faces"
faces_folder = "D:\\2016_USATF_Sprint_TrainingDataset"
myDetector="myDetector.svm"
myHOGDetector="myHOGDetector.svm"

o.train_object_detector(faces_folder,myTraining,myTesting,myDetector,myHOGDetector)