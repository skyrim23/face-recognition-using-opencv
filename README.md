# face-recognition-using-opencv
This project aims to develop an autonomous attendance system that uses face recognition technology to identify and verify individuals’ facial features and record attendance automatically.


# Before starting:
1. We have used android smartphone's camera as input to the program. For this you have to install 'IP webcam' app from playstore (https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en).

2. Make changes in student.xls file as per your requirement.

  Run the mainfile.py file and a small gui will appear on screen. 
  Click on 'Create Dataset' button to add new faces to dataset.Then it will ask for ID and name to enter. After that it starts to detect face and assigns the ID to that particular face (this is dataset creater hence only one face should be exposed before camera) and saves these .jpg file in a seperate folder named dataSet (folder should be created prior running the script) in the same directory.

   Click on 'Train' button to train the faces in datasets. It trains the model on the present dataset and creates trainingData.yml file in recognizer folder (folder should be created prior running the script). You will see IDs of dataset which are being trained in the consol of your python IDE.

  As the dataset has been trained you can now test it by clicking 'Detect' button. This will recognize the faces which has been trained and write attendance of the recognized students into the student.xls file.

  To show a bar graph of roll number vs attendance(%) click 'bar graph' button.
If you want students list whose attendance is less than 75% then click the 'detained students' button; the list will be saved in demo.xlsx excel sheet.


# Note: 
This model has been tested on windows 10, python 3.6 and opencv 3.4 and has accuracy of about 67%.
