using System;
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
        }

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
            string path = "test.py";//待处理python文件的路径，本例中放在debug文件夹下
            string sArguments = path;
            ArrayList arrayList = new ArrayList();
            arrayList.Add(url);//需要渗透的网站
            arrayList.Add(th);//线程数
            arrayList.Add("ASPX.txt");//调用字典
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
                //接受.py 进程打印的字符信息到文本显示框
                richTextBox1.AppendText(printedStr + "\n");
                label5.Text = "扫描结束";
            });
            Invoke(at);
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
