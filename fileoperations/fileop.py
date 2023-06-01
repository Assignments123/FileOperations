"""
Missing requirements.txt file
Missing .gitignore file
Missing docstrings to endpoints
Unneccesssary print statements
TASK 1 => when I encrypt file salad recipe.txt => encrypted file is created but no data present so when decrypt the same no data is retrieve => task 1 is fails
TASK 2 => `Update files in the destination directory if they exist in both directories but have different content` This is requirment
but progam does not update file but overwrite it meaning destination file content is repalced with source file content.
TASK 3 => It works good but for C:/ disk only but we can implement for other as well. Requirement specified to take folder
to search into but program take look into all folders - GOOD 
Frontend dev is GOOD 
"""
from flask import Flask,request,render_template
import os
from dotenv import load_dotenv

# for comparison of files
import filecmp
# for copying file from source to destination
import shutil
load_dotenv()
fileop = Flask(__name__)


@fileop.route('/')
def home():
    return render_template('base.html')

# task 3
@fileop.route('/findroot',methods=['POST'])
def findroot():
    
    rootdir = "C:/"
    flag = False
    filetosearch = request.form['filename']
    if filetosearch =="":
        msg="please give filename to search"
        return render_template('base.html',msg=msg)
    list = []

    for relpath,dirs,files in os.walk(rootdir):
        if(filetosearch in files):
            flag = True
            fullpath = os.path.join(rootdir,relpath,filetosearch)
            list.append(fullpath)
    if flag == True:
        return render_template('base.html',list=list)
    else:
        msg = "file with this name is not present"
        return render_template('base.html',msg=msg)

# task 2
@fileop.route('/syncpage')
def syncpage():
    return render_template('sync.html')
        
@fileop.route('/sync',methods=["POST"])
def synchronization():

    sourcedir = request.form['source']
    if sourcedir=="":
        msg = "Source Directory can not be empty"
        return render_template('sync.html',msg = msg)
    elif not os.path.exists(sourcedir):
        msg = "Source directory does not exist"
        return render_template('sync.html',msg = msg)
    
    destinationdir = request.form['destination']
    if destinationdir=="":
        msg = "Destination directory can not be empty"
        return render_template('sync.html',msg = msg)
    elif not os.path.exists(destinationdir):
        msg = "Destination directory does not exist"
        return render_template('sync.html',msg = msg)
    

    # file1 = "base.html"
    # file2 = "sync.html"
    copiedfiles = []
    removedfiles = []
    updatedfiles = []

    # if filecmp.cmp(file1,file2,shallow=True):
    #     print("files are same")
    # else:
    #     print("files are not same")
    
    print(sourcedir,destinationdir)
    # sourcedir= "C:/Users/manoj.kanadi/manoj/PYTHON/dir1"
    # destinationdir= "C:/Users/manoj.kanadi/manoj/PYTHON/dir2"
    val =filecmp.dircmp(sourcedir,destinationdir,ignore=None,hide=None)

    
    val.report()
    print("identical files are :\n",val.same_files)

    # code for copying source files into destination dir which are missin in destination dir
    for file in val.left_only:

        # copyfile = sourcedir+"/"+i
        copyfile2 = os.path.join(sourcedir,file)
        print("path 2 is \n "+copyfile2)
        destination = destinationdir
        # method will copy file into destination
        shutil.copy(copyfile2,destination)
        copiedfiles.append(file)
    print("copied files are : \n",copiedfiles)

    # code for deleting files which are only present in destination
    for file in val.right_only:
        removefile = file
        removefrom = destinationdir
        abspath = os.path.join(removefrom,removefile)
        os.remove(abspath)
        removedfiles.append(file)
    print("removed files are :",removedfiles)

    # same files = same name and same content
    # common files = same name content maybe same or different
    # different files = same name but different content
    # code for updating files with similar name but different content
    for file in val.diff_files:
        filename = file
        sourcepath = os.path.join(sourcedir,filename)
        destinationpath = os.path.join(destinationdir,filename)
        shutil.copyfile(sourcepath,destinationpath)
        updatedfiles.append(file)
    print("Updated files are :",updatedfiles)

    data = {}
    if len(copiedfiles)!=0:
        data['Copied files']=copiedfiles
    if len(removedfiles)!=0:
        data['Removed files']=removedfiles
    if len(updatedfiles)!=0:
        data['Updated files']=updatedfiles
    
    if len(data)!=0:

    # data = {
    #     "copied files":copiedfiles,
    #     "removed files":removedfiles,
    #     "updated files":updatedfiles
    # }
        return render_template('sync.html',data =data)
    else:
        msg = "No changes done because directories are already synchronized"
        return render_template('sync.html',msg =msg)





# task 1

# from cryptography.fernet import Fernet
@fileop.route('/secure')
def secure():
    return render_template('securefile.html')




@fileop.route('/securefile' ,methods=['POST'])
def securefile():
    
    # for creating a new key
    # key = Fernet.generate_key()
    # print(key)

    key = os.getenv('KEY')
    print("key is : ",key)
    # firstfile = "trial.txt"
    # secondfile = "trial2.txt"

    firstfile = request.form['firstfile']
    
    print(firstfile)
    
    secondfile = request.form['secondfile']

    command = request.form['command']
    
    
    # command = "decrypt"

    # create object fernet class
    # f = Fernet(key)

    if command == "encrypt":

        if not os.path.isfile(firstfile):
            message= "file is not present"
            return render_template('securefile.html',message = message)

        # code for encrypting the normal data
        encryptfile = open(firstfile,'r')
        data = encryptfile.read()
        print("data",data)
        # using cryptography package
        # encrypted = f.encrypt(data)
        # print(encrypted)
        # encryptedfile = open(secondfile,'wb')
        # encryptedfile.write(encrypted)


        # using substitution cypher algorithm
        encrypteddata = ""
        for char in data:
            
            if char.isalpha():
                if char.isupper():
                    print(char)
                    # encrypted = str(key[ord(char) -ord('A')]).upper
                    encrypted = key[ord(char) - ord('A')].upper()
                    encrypteddata = encrypteddata + encrypted
                else:
                    # encrypted = str(key[ord(char) - ord('a')]).lower
                    encrypted = key[ord(char) - ord('a')].lower()
                    encrypteddata = encrypteddata + encrypted
            else:
                 encrypteddata = encrypteddata + char 
        encryptedfile = open(secondfile,'w')        # opened file but not closed it, take look at how to write into file
        encryptedfile.write(encrypteddata)

        message = "file is encrypted"

        return render_template('securefile.html',message = message)

    elif command == "decrypt":

        if not os.path.isfile(firstfile):
            message= "file is not present"
            return render_template('securefile.html',message = message)

        # code for decrypting the data
        # dont use rb mode because it gives ascii values
        decryptfile = open(firstfile,'r')
        data = decryptfile.read()

        # decrypted = f.decrypt(data)
        # print("decrypted data is : ",decrypted)
         
        decrypteddata = ""
        for char in data:
            # char = str(char)
            if char.isalpha():
                if char.isupper():
                    decrypted = chr(key.upper().index(char) + ord('A'))
                    decrypteddata += decrypted
                else:
                    decrypted = chr(key.lower().index(char) + ord('a'))
                decrypteddata += decrypted
            else:
                decrypteddata += char

        decryptfile = open(secondfile,'w')
        decryptfile.write(decrypteddata)

        message = "file is decrypted"
        return render_template('securefile.html',message = message)

    return render_template('securefile.html')

if __name__ == "__main__":  # standard way to run file
    fileop.run(debug=True)