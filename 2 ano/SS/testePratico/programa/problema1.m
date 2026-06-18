%problema 1
clear;
%1)
Fs = 10000;
Ts = 1/Fs;

T = 0.1
N = Fs*T ;%numero de amostras em 0.1 sec

t = (0:N-1)*(Ts/2);
x = 2*cos(150*pi*t) + sin(300*pi*t) + 0.5*cos(450*pi*t);
%2)
figure(1);
plot(t,x);
xlabel("Time (s)");
ylabel("Signal Amlitude");
title("x signal (freq to time)");
grid on;

%3)
X = fft(x);%time to freq

f =(0:N-1)*(Fs/N);%the Fs is broken to 1000 pieces for xaxis

Mag = abs(X)/N; %max magnitude that the signal can reach?
figure(99);
stem(f,Mag);
%mag sample
one_sided_mag = Mag(1:(N/2)+1);%Nquits f >= 450 but use 500(N/2 amostras), the 1 is to exclude 0

one_sided_mag(2:end -1) = 2 * one_sided_mag(2:end -1);

f_addabted = f(1:N/2+1);

figure(2);
%plot(f,Mag);
stem(f_addabted,one_sided_mag);%x and y must have thr same size
xlabel("Freq (Hz)");
ylabel("Signal magnitude");
title("x signal (time to freq)");
grid on;
xlim([0, 600]);

%4)
%para determinar os picos temos que aomentar a resolusao que se faz diminuindo Ts ou aumentando T
peaks1 =[];
freq_of_peaks = []
nPeaks = 0;
for i = 2:length(one_sided_mag)-1
  if Mag(i)> 0.01
    if one_sided_mag(i)> one_sided_mag(i-1) && one_sided_mag(i + 1) < one_sided_mag(i)
      peaks1 = [peaks1,one_sided_mag(i)];
      freq_of_peaks = [freq_of_peaks,f_addabted(i)];
      nPeaks = nPeaks + 1;
    end
  end
end


printf("%d\n",peaks1);
printf("foram detetados %d picos",nPeaks);
printf("no(s) índice(s) %d, %d, %d \n",peaks1(1),peaks1(2),peaks1(3));

%5)

Hz = [];
Hz =  peaks1/freq_of_peaks;
for k  = 1 :length(peaks1)
  Hz = [Hz,peaks1(k)/freq_of_peaks(k)];
end
printf("As frequências presentes no sinal são: %d, %d e %d",Hz(1),Hz(2),Hz(3));
