﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using System.Net;
using System.Net.Sockets;
using IronPython.Hosting;
using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;
using System.Collections;
using System.Diagnostics;


namespace temperature_control
{
    public partial class Form1 : Form
    {
        private Queue<double> dataQueue = new Queue<double>(100);
        public Form1()
        {
            InitializeComponent();
        }
        public delegate void DelegateChangeText(string Messages);
    

        private void Form1_Load(object sender, EventArgs e)
        {
            skinEngine1.SkinFile = "DiamondBlue.ssk";//加载winform皮肤
            textBox1.Text = "http://www.baidu.com";
            textBox7.Text = "http://10.16.53.180/pikachu/vul/burteforce/bf_form.php";
            textBox8.Text = "test";
        }
/// <summary>
/// 目录开始扫描
/// </summary>
/// <param name="sender"></param>
/// <param name="e"></param>
        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            runPythonP();//运行python函数
            label5.Text = "开始扫描...";
        }
        Process p;

        /// <summary>
        /// 调用python脚本
        /// </summary>
        void runPythonP()
        {
            string th = comboBox1.Text;
            string url = textBox1.Text;
            p = new Process();
            string path = "Directory-scanning.py";//待处理python文件的路径，本例中放在debug文件夹下
            string sArguments = path;
            ArrayList arrayList = new ArrayList();
            arrayList.Add(url);//需要渗透的网站
            arrayList.Add(th);//线程数
            arrayList.Add("php.txt");//调用字典
            foreach (var param in arrayList)//拼接参数
            {
                sArguments += " " + param;
            }
            p.StartInfo.FileName = @"D:\Anaconda\python.exe"; //没有配环境变量的话，可以写"xx\xx\python.exe"的绝对路径。如果配了，直接写"python"即可
            p.StartInfo.Arguments = sArguments;//python命令的参数
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            p.Start();//启动进程
            //MessageBox.Show("启动成功");
            p.BeginOutputReadLine();
            p.OutputDataReceived += new DataReceivedEventHandler(p_OutputDataReceived);
            Console.ReadLine();
            //p.WaitForExit();
        }
  
        void p_OutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            var printedStr = e.Data;
            Action at = new Action(delegate ()
            {
                //接受.py进程打印的字符信息到文本显示框
                richTextBox1.AppendText(printedStr + "\n");
                label5.Text = "扫描结束";
            });
            Invoke(at);
        }
/// <summary>
/// 端口开始扫描
/// </summary>
/// <param name="sender"></param>
/// <param name="e"></param>
        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
            runPythonScan();//运行python函数
            label17.Text = "开始扫描...";
        }
        void runPythonScan()
        {
            string ip = textBox2.Text;
            string thread = comboBox4.Text;
            string time = comboBox2.Text;
            string type = comboBox5.Text;
            string port_start = textBox3.Text;
            string port_end = textBox4.Text;
            p = new Process();
            string path = "port_scan.py";//待处理python文件的路径，本例中放在debug文件夹下
            string sArguments = path;
            ArrayList arrayList = new ArrayList();
            arrayList.Add(ip);//需要渗透的网站
            arrayList.Add(thread);//线程数
            arrayList.Add(time);//超时时间
            arrayList.Add(type);//扫描类型
            arrayList.Add(port_start);//起始端口
            arrayList.Add(port_end);//终止端口
            foreach (var param in arrayList)//拼接参数
            {
                sArguments += " " + param;
            }
            p.StartInfo.FileName = @"D:\Anaconda\python.exe"; //没有配环境变量的话，可以写"xx\xx\python.exe"的绝对路径。如果配了，直接写"python"即可
            p.StartInfo.Arguments = sArguments;//python命令的参数
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            p.Start();//启动进程
            //MessageBox.Show("启动成功");
            p.BeginOutputReadLine();
            p.OutputDataReceived += new DataReceivedEventHandler(p_OutputDataReceived_scan);
            Console.ReadLine();
            //p.WaitForExit();
        }

        void p_OutputDataReceived_scan(object sender, DataReceivedEventArgs e)
        {
            var printedStr = e.Data;
            Action at = new Action(delegate ()
            {
                //接受.py进程打印的字符信息到文本显示框
                richTextBox2.AppendText(printedStr + "\n");
                label17.Text = "扫描结束";
            });
            Invoke(at);
        }
        /// <summary>
        /// 暴力破解
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox3.Clear();
            runPythonPassword();//运行python函数
            label19.Text = "开始扫描...";
        }
        void runPythonPassword()
        {

            string url ="http://10.16.53.180/pikachu/vul/burteforce/bf_form.php";
            //string headers = richTextBox4.Text;
            string username = textBox8.Text;
            p = new Process();
            string path = "trans_headers.py";//待处理python文件的路径，本例中放在debug文件夹下
            string sArguments = path;
            ArrayList arrayList = new ArrayList();
            arrayList.Add(url);//网站url
            //arrayList.Add(headers);//请求头
            arrayList.Add(username);//破解的用户名
            foreach (var param in arrayList)//拼接参数
            {
                sArguments += " " + param;
            }
            //label29.Text = sArguments;
            p.StartInfo.FileName = @"D:\Anaconda\python.exe"; //没有配环境变量的话，可以写"xx\xx\python.exe"的绝对路径。如果配了，直接写"python"即可
            p.StartInfo.Arguments = sArguments;//python命令的参数
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            p.Start();//启动进程
            //MessageBox.Show("启动成功");
            p.BeginOutputReadLine();
            p.OutputDataReceived += new DataReceivedEventHandler(p_OutputDataReceived_password);
            Console.ReadLine();
            //p.WaitForExit();
        }

        void p_OutputDataReceived_password(object sender, DataReceivedEventArgs e)
        {
            var printedStr = e.Data;
            Action at = new Action(delegate ()
            {
                //接受.py进程打印的字符信息到文本显示框
                richTextBox3.AppendText(printedStr + "\n");
                label19.Text = "扫描结束";
            });
            Invoke(at);
        }
    }
}
