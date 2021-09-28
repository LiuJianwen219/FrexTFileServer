import logging
import os
import socket
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from FrexTFileServer.settings import rootFileDir, DEBUG, rootFileDirDebug

rootPath = rootFileDir if DEBUG is False else rootFileDirDebug

# get path
# cur_dir = os.path.abspath(__file__).rsplit("/", 1)[0]
log_path = os.path.join(rootPath, "FrexTFileServer_" + socket.gethostname() + ".log")

# encoding='utf-8'
logging.basicConfig(filename=log_path, level=logging.DEBUG,
                    filemode='w', format='%(levelname)s:%(asctime)s:%(message)s',
                    datefmt='%Y-%d-%m %H:%M:%S')
logging.debug('Welcome to use FrexT File System!')
logging.info('This component a sub component of FrexT project.')
logging.warning('Providing file operations,')
logging.error('Current version is v1.0.0,')
logging.critical("For helping, please see localhost:8010/help/")
logger = logging.getLogger(__name__)


# read file interface, maybe DFS future
def file_reader(file_path):
    if os.path.exists(file_path):
        file = open(file_path, 'rb')
        file_content = file.read()
        file.close()
        return file_content
    logger.error("Read Question error: file not found: " + file_path)
    return None


# write file interface, maybe DFS future
def file_writer(fire_dir, file_name, file_content):
    if not os.path.exists(fire_dir):
        os.makedirs(fire_dir)
    with open(os.path.join(fire_dir, file_name), 'wb+') as destination:
        for chunk in file_content.chunks():
            destination.write(chunk)


# delete file interface, maybe DFS future
def file_deleter(fire_dir, file_name):
    if os.path.exists(os.path.join(fire_dir, file_name)):
        os.remove(os.path.join(fire_dir, file_name))


@csrf_exempt
def tcls(request):
    tclName = "main"
    if request.method == "GET":
        fileDir = os.path.join(rootPath, "sys", "testing")
        fileName = tclName + ".tcl"
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Tcl: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}.tcl"'.format(tclName)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        fileDir = os.path.join(rootPath, "sys", "testing")
        fileName = tclName + ".tcl"
        logger.info("Write Tcl: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("tcl file save complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for TCL.")
    response["status"] = "failed"
    return response


@csrf_exempt
def questions(request):
    if request.method == "GET":
        testId = request.GET.get("testId")
        topic = request.GET.get("topic")
        fileDir = os.path.join(rootPath, "sys", "testing", testId)
        fileName = topic + ".zip"
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Question: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}.zip"'.format(topic)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        testId = request.POST.get("testId")
        topic = request.POST.get("topic")
        fileDir = os.path.join(rootPath, "sys", "testing", testId)
        fileName = topic + ".zip"
        logger.info("Write Question: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("question file save complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for QUESTION.")
    response["status"] = "failed"
    return response


@csrf_exempt
def tests(request):
    if request.method == "GET":
        userId = request.GET.get("userId")
        testId = request.GET.get("testId")
        submitId = request.GET.get("submitId")
        topic = request.GET.get("topic")
        fileDir = os.path.join(rootPath, "user", userId, "testing", testId, submitId)
        fileName = topic + ".v"
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Test: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}.v"'.format(topic)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        userId = request.POST.get("userId")
        testId = request.POST.get("testId")
        submitId = request.POST.get("submitId")
        topic = request.POST.get("topic")
        fileDir = os.path.join(rootPath, "user", userId, "testing", testId, submitId)
        fileName = topic + ".v"
        logger.info("Write Test: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("test file save complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for TEST.")
    response["status"] = "failed"
    return response


@csrf_exempt
def bits(request):
    if request.method == "GET":
        userId = request.GET.get("userId")
        testId = request.GET.get("testId")
        submitId = request.GET.get("submitId")
        topic = request.GET.get("topic")
        fileDir = os.path.join(rootPath, "user", userId, "testing", testId, submitId, "output")
        fileName = topic + ".bit"
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Bit: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}.bit"'.format(topic)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        userId = request.POST.get("userId")
        testId = request.POST.get("testId")
        submitId = request.POST.get("submitId")
        topic = request.POST.get("topic")
        fileDir = os.path.join(rootPath, "user", userId, "testing", testId, submitId, "output")
        fileName = topic + ".bit"
        logger.info("Write Bit: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("bit file save complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for BIT.")
    response["status"] = "failed"
    return response


@csrf_exempt
def logs(request):
    if request.method == "GET":
        userId = request.GET.get("userId")
        testId = request.GET.get("testId")
        submitId = request.GET.get("submitId")
        topic = request.GET.get("topic")
        fileDir = os.path.join(rootPath, "user", userId, "testing", testId, submitId, "output")
        fileName = topic + ".log"
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Log: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}.log"'.format(topic)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        userId = request.POST.get("userId")
        testId = request.POST.get("testId")
        submitId = request.POST.get("submitId")
        topic = request.POST.get("topic")
        fileDir = os.path.join(rootPath, "user", userId, "testing", testId, submitId, "output")
        fileName = topic + ".log"
        logger.info("Write Log: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("log file save complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for LOG.")
    response["status"] = "failed"
    return response


@csrf_exempt
def results(request):
    if request.method == "GET":
        userId = request.GET.get("userId")
        testId = request.GET.get("testId")
        submitId = request.GET.get("submitId")
        topic = request.GET.get("topic")
        fileDir = os.path.join(rootPath, "user", userId, "testing", testId, submitId, "output")
        fileName = topic + ".result"
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Result: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}.result"'.format(topic)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        userId = request.POST.get("userId")
        testId = request.POST.get("testId")
        submitId = request.POST.get("submitId")
        topic = request.POST.get("topic")
        fileDir = os.path.join(rootPath, "user", userId, "testing", testId, submitId, "output")
        fileName = topic + ".result"
        logger.info("Write Result: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("result file save complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for RESULT.")
    response["status"] = "failed"
    return response


@csrf_exempt
def experiment(request):
    if request.method == "GET":
        userId = request.GET.get("userId", None)
        experimentType = request.GET.get("experimentType", None)
        experimentId = request.GET.get("experimentId", None)
        fileName = request.GET.get("fileName", None)

        fileDir = os.path.join(rootPath, "user", userId, "online", "experiment",
                               experimentType, experimentId)
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Experiment: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(fileName)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        userId = request.POST.get("userId", None)
        experimentType = request.POST.get("experimentType", None)
        experimentId = request.POST.get("experimentId", None)
        fileName = request.POST.get("fileName", None)

        fileDir = os.path.join(rootPath, "user", userId, "online", "experiment",
                               experimentType, experimentId)
        logger.info("Write Result: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("experiment file save complete!")
        response["status"] = "success"
        return response

    elif request.method == "DELETE":
        delete = QueryDict(request.body)
        userId = delete.get('userId')
        experimentType = delete.get('experimentType')
        experimentId = delete.get('experimentId')
        fileName = delete.get('fileName')

        fileDir = os.path.join(rootPath, "user", userId, "online", "experiment",
                               experimentType, experimentId)
        logger.info("Delete Result: " + fileDir + fileName)

        file_deleter(fileDir, fileName)

        response = HttpResponse("experiment file delete complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for EXPERIMENT.")
    response["status"] = "failed"
    return response


@csrf_exempt
def online_bits(request):
    if request.method == "GET":
        userId = request.GET.get("userId")
        experimentType = request.GET.get("experimentType", None)
        experimentId = request.GET.get("experimentId", None)
        compileId = request.GET.get("compileId", None)

        fileDir = os.path.join(rootPath, "user", userId, "online", "experiment",
                               experimentType, experimentId, "output")
        fileName = compileId + ".bit"
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Bit: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}.bit"'.format(compileId)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        userId = request.POST.get("userId")
        experimentType = request.POST.get("experimentType", None)
        experimentId = request.POST.get("experimentId", None)
        compileId = request.POST.get("compileId", None)

        fileDir = os.path.join(rootPath, "user", userId, "online", "experiment",
                               experimentType, experimentId, "output")
        fileName = compileId + ".bit"
        logger.info("Write Bit: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("bit file save complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for BIT.")
    response["status"] = "failed"
    return response


@csrf_exempt
def own_bits(request):
    if request.method == "GET":
        userId = request.GET.get("userId")
        experimentType = request.GET.get("experimentType", None)
        experimentId = request.GET.get("experimentId", None)
        fileName = request.GET.get("fileName", None)

        fileDir = os.path.join(rootPath, "user", userId, "online", "experiment",
                               experimentType, experimentId)
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Bit: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(fileName)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        userId = request.POST.get("userId")
        experimentType = request.POST.get("experimentType", None)
        experimentId = request.POST.get("experimentId", None)
        fileName = request.POST.get("fileName", None)

        fileDir = os.path.join(rootPath, "user", userId, "online", "experiment",
                               experimentType, experimentId)
        logger.info("Write Bit: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("bit file save complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for BIT.")
    response["status"] = "failed"
    return response


@csrf_exempt
def online_logs(request):
    if request.method == "GET":
        userId = request.GET.get("userId")
        experimentType = request.GET.get("experimentType", None)
        experimentId = request.GET.get("experimentId", None)
        compileId = request.GET.get("compileId", None)

        print(userId)
        print(experimentType)
        print(experimentId)
        print(compileId)

        fileDir = os.path.join(rootPath, "user", userId, "online", "experiment",
                               experimentType, experimentId, "output")
        fileName = compileId + ".log"
        filePath = os.path.join(fileDir, fileName)
        logger.info("Read Log: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="{0}.log"'.format(compileId)
        response["filePath"] = filePath
        response["fileName"] = fileName
        response["status"] = "success" if file is not None else "failed"
        return response

    elif request.method == "POST":
        userId = request.POST.get("userId")
        experimentType = request.POST.get("experimentType", None)
        experimentId = request.POST.get("experimentId", None)
        compileId = request.POST.get("compileId", None)

        print(userId)
        print(experimentType)
        print(experimentId)
        print(compileId)

        fileDir = os.path.join(rootPath, "user", userId, "online", "experiment",
                               experimentType, experimentId, "output")
        fileName = compileId + ".log"
        logger.info("Write Log: " + fileDir + fileName)

        file_writer(fileDir, fileName, request.FILES["file"])

        response = HttpResponse("log file save complete!")
        response["status"] = "success"
        return response

    response = HttpResponse("unknown http action type for LOG.")
    response["status"] = "failed"
    return response


def help(request):
    if request.method == "GET":
        helpFileName = "help"
        fileType = request.GET.get("type") if request.GET.get("type") is not None else "md"
        filePath = os.path.join(helpFileName + "." + fileType)
        logger.info("Read help: " + filePath)

        file = file_reader(filePath)

        response = HttpResponse(file)
        response['Content-Type'] = "text/plain;charset=utf-8"  # 设置头信息，告诉浏览器这是个文件
        # response['Content-Disposition'] = 'attachment;filename="{0}.{1}"'.format(helpFileName, type)
        response["filePath"] = filePath
        response["fileName"] = helpFileName
        response["status"] = "success" if file is not None else "failed"
        return response

    response = HttpResponse("please use GET to see the help file.")
    response["status"] = "failed"
    return response


def ping(request):
    return HttpResponse("pong")
