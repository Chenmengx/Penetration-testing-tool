using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Net.Sockets;
using System.Net;
using System.Threading;
using System.IO;

namespace temperature_control
{
    static class Program
    {
        /// <summary>
        /// 应用程序的主入口点。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
    }
    public class UDPServerClass
    {
        public delegate void MessageHandler(string Message);//定义委托事件  
        public event MessageHandler MessageArrived;
        public UDPServerClass()
        {
            //获取本机可用IP地址  
            IPAddress[] ips = Dns.GetHostAddresses(Dns.GetHostName());
            foreach (IPAddress ipa in ips)
            {
                if (ipa.AddressFamily == AddressFamily.InterNetwork)
                {
                    MyIPAddress = ipa;//获取本地IP地址  
                    break;
                }
            }
            Note_StringBuilder = new StringBuilder();
            PortName = 8080;//端口

        }
        public UdpClient ReceiveUdpClient;

        /// <summary>  
        /// 侦听端口名称  
        /// </summary>  
        public int PortName;

        /// <summary>  
        /// 本地地址  
        /// </summary>  
        public IPEndPoint LocalIPEndPoint;

        /// <summary>  
        /// 日志记录  
        /// </summary>  
        public StringBuilder Note_StringBuilder;
        /// <summary>  
        /// 本地IP地址  
        /// </summary>  
        public IPAddress MyIPAddress;

        public void Thread_Listen()
        {
            //创建一个线程接收远程主机发来的信息  
            Thread myThread = new Thread(ReceiveData);
            myThread.IsBackground = true;
            myThread.Start();
        }

        /// <summary>
        /// 将ByteToString
        /// </summary>
        /// <param name="DataByte"></param>
        /// <returns></returns>
        private string ByteToString(byte[] DataByte)
        {
            string result = "";
            foreach (var DB in DataByte)
            {
                string a;
                string b;
                switch ((DB & 0x0f).ToString())
                {
                    case "10":
                        a = "A";
                        break;
                    case "11":
                        a = "B";
                        break;
                    case "12":
                        a = "C";
                        break;
                    case "13":
                        a = "D";
                        break;
                    case "14":
                        a = "E";
                        break;
                    case "15":
                        a = "F";
                        break;
                    default:
                        a = (DB & 0x0f).ToString();
                        break;


                }
                switch ((DB >> 4 & 0x0f).ToString())
                {
                    case "10":
                        b = "A";
                        break;
                    case "11":
                        b = "B";
                        break;
                    case "12":
                        b = "C";
                        break;
                    case "13":
                        b = "D";
                        break;
                    case "14":
                        b = "E";
                        break;
                    case "15":
                        b = "F";
                        break;
                    default:
                        b = (DB >> 4 & 0x0f).ToString();
                        break;
                }

                result += b + a;
                result += "";
            }
            result += "C";
            return result;
        }
        /// <summary>  
        /// 接收数据  
        /// </summary>  
        private void ReceiveData()
        {
            IPEndPoint local = new IPEndPoint(MyIPAddress, PortName);
            ReceiveUdpClient = new UdpClient(local);
            IPEndPoint remote = new IPEndPoint(IPAddress.Any, 0);
            while (true)
            {
                try
                {
                    //关闭udpClient 时此句会产生异常  
                    byte[] receiveBytes = ReceiveUdpClient.Receive(ref remote);
                    string receiveMessage = Encoding.Default.GetString(receiveBytes, 0, receiveBytes.Length);
                    string str = ByteToString(receiveBytes);
                    //  receiveMessage = ASCIIEncoding.ASCII.GetString(receiveBytes, 0, receiveBytes.Length);  
                    MessageArrived(string.Format("{0}来自{1}:{2}", DateTime.Now.ToString(), remote, str));
  



                    //try  
                    //{  
                    //    Byte[] sendBytes = Encoding.ASCII.GetBytes("Is anybody there?");  
                    //    ReceiveUdpClient.Send(sendBytes, sendBytes.Length, local);  
                    //}  
                    //catch (Exception e)  
                    //{  
                    //}  
                    //break;  

                }
                catch
                {
                    break;
                }
            }
        }

        /// <summary>  
        /// 添加日志信息到Note_StringBuilder  
        /// </summary>  
        public void AddMessage_Note_StringBuilder()
        {

        }
    }
    }
