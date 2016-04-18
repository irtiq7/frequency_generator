import pyaudio
import numpy as np
from Tkinter import *

p = pyaudio.PyAudio()


class Soundgenerator(object):
	def __init__(self, master):
		self.master = master
		master.title("VINAYA TECHNOLOGIES")
		self.initialising(master)
	
	def initialising(self, master):
		self.entryVar_freq_box = DoubleVar()
		self.entryVar_samp_freq = IntVar()
		self.entryVar_duration = DoubleVar()
		self.entryVar_volume = DoubleVar()
		
		self.label_title = Label(master, text="FREQUENCY GENERATOR", font = "-weight bold").grid(row=0, column=0, columnspan =2)
		self.label_freq_box = Label(master, text="FREQUENCY OF THE WAVE (Hz)").grid(row=1, column=0)
		self.entry_freq_box = Entry(master, textvariable=self.entryVar_freq_box).grid(row=1, column=1)
		self.label_samp_freq = Label(master, text="SAMPLING FREQUENCY (Hz)").grid(row=2, column=0)
		self.entry_samp_freq = Entry(master,textvariable=self.entryVar_samp_freq).grid(row=2, column=1)
		self.label_duration = Label(master, text = "DURATION (s)").grid(row=3, column=0)
		self.entry_duration = Entry(master,textvariable=self.entryVar_duration).grid(row=3, column=1)
		self.label_volumne = Label(master, text="VOLUME [0.1 - 1.0]").grid(row=4, column=0)
		self.entry_volume = Entry(master,textvariable=self.entryVar_volume).grid(row=4, column=1)
		self.button = Button(master, text = "GENERATE", command=self.cal_data).grid(row=5, column=0, columnspan=2)

		self.entryVar_freq_box.set('25')
		self.entryVar_samp_freq.set('44100')
		self.entryVar_duration.set('1')
		self.entryVar_volume.set('0.3')

	def cal_data(self):
		self.f = (self.entryVar_freq_box.get())     # range [0.0, 1.0]
		self.fs = (self.entryVar_samp_freq.get())       # sampling rate, Hz, must be integer
		self.duration = (self.entryVar_duration.get())  # in seconds, may be float
		self.volume = (self.entryVar_volume.get())        # sine frequency, Hz, may be float
				
		# generate samples, note conversion to float32 array
		samples = (np.sin(2*np.pi*np.arange(self.fs*self.duration)*self.f/self.fs)).astype(np.float32)

		# for paFloat32 saample values must be in range [-1.0, 1.0]
		stream = p.open(format=pyaudio.paFloat32,
						channels=1,
						rate=self.fs,
						output=True)

		# play. May repeat with different volume values (if done interactively) 

		stream.write(self.volume*samples)

		stream.stop_stream()
		stream.close()

		#~ p.terminate()

root = Tk()
Soundgenerator(root)
root.mainloop()
