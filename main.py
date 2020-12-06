import re
import subprocess
import sys

from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QMenu, QAction
from netifaces import ifaddresses, interfaces, AF_INET

from ui import Ui_MainWindow


class MySignals(QObject):
    signal = Signal(object)


class QMain(QMainWindow):

    def __init__(self):
        super(QMain, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 过滤掉未获取到IP地址的适配器
        self.ip_address_list = sorted([a for a in self.get_all_ip_address() if a[:3] != '169'])
        self.ui.listenaddress.addItems(self.ip_address_list)
        self.ui.connectaddress.addItems(self.ip_address_list)
        self.update_network_list = MySignals()
        # 信号连接槽，需要更新端口转发地址时发送信号触发函数调用
        self.update_network_list.signal.connect(self.get_all_network)  # noqa
        self.get_all_network()
        self.check_service_status()

    @staticmethod
    def get_all_ip_address():
        """
        获取本机所有的IP地址

        :return: IP地址列表
        """
        return [ifaddresses(a)[AF_INET][0]['addr'] for a in interfaces() if (AF_INET in ifaddresses(a))]

    def start(self):
        """
        运行程序

        :return: None
        """
        network = self.ui.network.currentText()
        listen_address = self.ui.listenaddress.currentText()
        listen_port = self.ui.listenport.text()
        connect_address = self.ui.connectaddress.currentText()
        connect_port = self.ui.connectport.text()
        if self.check_ip_port(listen_address, listen_port, connect_address, connect_port):
            command = 'netsh interface portproxy add %s listenaddress=%s listenport=%s connectaddress=%s connectport=%s'  # noqa
            command = command % (network, listen_address, listen_port, connect_address, connect_port)
            self.run_and_check_result(command)
            # 执行命令结束发出信号更新network_list
            self.update_network_list.signal.emit(True)  # noqa

    def check_ip_port(self, listen_address, listen_port, connect_address, connect_port):
        """
        检测IP地址和端口是否合法

        :param listen_address: 监听地址
        :param listen_port: 监听端口
        :param connect_address: 连接地址
        :param connect_port: 连接端口
        :return: bool
        """
        if not (listen_address and listen_port and connect_address and connect_port):
            text = ''
            if not listen_address:
                text += '监听地址，'
            if not listen_port:
                text += '监听端口，'
            if not connect_address:
                text += '连接地址，'
            if not connect_port:
                text += '连接端口，'
            QMessageBox.warning(self, '提示', f'{text[:-1]}不能为空！', QMessageBox.Ok, QMessageBox.Ok)
            return False
        rule_ipaddress = re.compile(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$')
        rule_port = re.compile(
            r'^[1-9]$|(^[1-9][0-9]$)|(^[1-9][0-9][0-9]$)|(^[1-9][0-9][0-9][0-9]$)|(^[1-6][0-9][0-9][0-9][0-9]$)')
        if rule_ipaddress.match(listen_address) and rule_ipaddress.match(connect_address) and \
                rule_port.match(listen_port) and rule_port.match(connect_port):
            if 1 <= int(listen_port) <= 65535 and 1 <= int(connect_port) <= 65535:
                return True
            else:
                if not (1 <= int(listen_port) <= 65535):
                    QMessageBox.warning(self, '提示', '监听端口不合法！', QMessageBox.Ok, QMessageBox.Ok)
                    return False
                if not (1 <= int(connect_port) <= 65535):
                    QMessageBox.warning(self, '提示', '连接端口不合法！', QMessageBox.Ok, QMessageBox.Ok)
                    return False
        else:
            text = ''
            if not rule_ipaddress.match(listen_address):
                text += '监听地址，'
            if not rule_ipaddress.match(connect_address):
                text += '连接地址，'
            if not rule_port.match(listen_port):
                text += '监听端口，'
            if not rule_port.match(connect_port):
                text += '连接端口，'
            QMessageBox.warning(self, '提示', f'{text[:-1]}不合法！', QMessageBox.Ok, QMessageBox.Ok)
            return False

    def run_and_check_result(self, command):
        """
        运行程序并且检测返回结果

        :param command: 需要运行的命令
        :return: None
        """
        stdout_data, stderr_data = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                    stdin=subprocess.PIPE,  # GUI程序中记得设置标准输入
                                                    shell=False).communicate()
        stdout_data = stdout_data.decode('gbk')
        stderr_data = stderr_data.decode('gbk')
        if stdout_data == '请求的操作需要提升(作为管理员运行)。\n\r\n':
            QMessageBox.warning(self, '提示', '请使用管理员权限运行程序！', QMessageBox.Ok, QMessageBox.Ok)
        elif stdout_data == '\r\n' and stderr_data == '':
            QMessageBox.information(self, '提示', 'OK!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(self, '提示', f'{stdout_data}\r\n{stderr_data}', QMessageBox.Ok, QMessageBox.Ok)

    def edit_item(self, item: QListWidgetItem):
        """
        编辑IP和端口

        :param item: 选中的item
        :return: None
        """
        src, des = item.text().split(' -> ')
        src_ip, src_port = src.split(':')
        des_ip, des_port = des.split(':')
        self.ui.listenaddress.setCurrentText(src_ip)
        self.ui.listenport.setText(src_port)
        self.ui.connectaddress.setCurrentText(des_ip)
        self.ui.connectport.setText(des_port)

    def get_all_network(self):
        """
        获取所有的网络适配器中包含的地址

        :return: None
        """
        # 先清空之前的值，再更新
        self.ui.network_list.clear()
        parent = r'(\S+?)\s+?(\d+?) \s+?(\S+?)\s+?(\d+?)\s+?'
        get_ip_port = re.compile(parent, re.VERBOSE)
        command = 'netsh interface portproxy show all'  # noqa
        stdout_data, stderr_data = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                    stdin=subprocess.PIPE,
                                                    shell=True).communicate()
        stdout_data, stderr_data = stdout_data.decode('gbk'), stderr_data.decode('gbk')
        result = re.findall(get_ip_port, stdout_data)
        for a in result:
            self.ui.network_list.addItem(f'{a[0]}:{a[1]} -> {a[2]}:{a[3]}')

    def my_listwidget_context(self, position):  # noqa
        """
        右键菜单

        :param position: 选中的条目索引
        :return: None
        """
        # 只有在选中item时才会出现菜单
        if self.ui.network_list.itemAt(position):
            menu = QMenu()
            del_act = QAction("删除", self)
            del_act.triggered.connect(self.del_network)  # noqa
            menu.addAction(del_act)
            menu.exec_(self.ui.network_list.mapToGlobal(position))

    def del_network(self):
        """
        删除数据

        :return: None
        """
        ip, port = self.ui.network_list.currentItem().text().split(' -> ')[0].split(':')
        command = f'netsh interface portproxy delete {self.ui.network.currentText()} listenaddress={ip} listenport={port}'  # noqa
        self.run_and_check_result(command)
        # 执行命令结束发出信号更新network_list
        self.update_network_list.signal.emit(True)  # noqa

    def check_service_status(self):
        """
        检查端口转发所需服务状态

        :return: None
        """
        command = 'sc query iphlpsvc'  # noqa
        stdout_data, stderr_data = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                                    stderr=subprocess.PIPE, shell=True).communicate()
        stdout_data, stderr_data = stdout_data.decode('gbk'), stderr_data.decode('gbk')
        print(stdout_data, stderr_data)
        if stdout_data:
            service_status = re.compile(r'STATE\s+?:\s+?(\d)').search(stdout_data).group(1)
            if service_status == '4':
                self.setWindowTitle(f'{self.windowTitle()}  服务状态：运行')
                return
            if service_status == '1':
                self.setWindowTitle(f'{self.windowTitle()}  服务状态：停止')
                return
            else:
                self.setWindowTitle(f'{self.windowTitle()}  服务状态：未知')
                return
        else:
            self.setWindowTitle(f'{self.windowTitle()}  服务状态：未知')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = QMain()
    s.show()
    sys.exit(app.exec_())
