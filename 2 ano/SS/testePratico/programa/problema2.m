%problema2
clear;


%1)
Fs = 20000;
Ts = 1 / Fs;
T = 0.05;% 0.05
N = (T) / Ts;% N amostras
t =(0:N-1)*Ts

x = cos(2*pi*800*t);

figure(1);
plot(t,x);
grid on;

%2)
figure(2);
Fs4 = 400;% a frequencia de amostragem tem de ser superior a 1600 hz nyquits
Fs12 = 1200;
Fs32 = 3200;

Ts4 = 1 / Fs4;
Ts12 = 1 / Fs12;
Ts32 = 1 / Fs32;

N4 = (T/1) / Ts4;
N12 = (T/1) / Ts12;
N32 = (T/1) / Ts32;

subplot(4,1,1);
plot(t,x);
ylabel("amplitude");
xlabel("time");
title("original signal");
grid on;

subplot(4,1,2);
t1 =(0:N4-1)*Ts4
x4 = cos(2*pi*800*t1);
plot(t1,x4);
ylabel("amplitude");
xlabel("time");
title("400Hz");

subplot(4,1,3);
t1 =(0:N12-1)*Ts12
x12 = cos(2*pi*800*t1);
plot(t1,x12);
ylabel("amplitude");
xlabel("time");
title("1200Hz");

subplot(4,1,4);
t1 =(0:N32-1)*Ts32
x32 = cos(2*pi*800*t1);
plot(t1,x32);
ylabel("amplitude");
xlabel("time");
title("3200");

%3)
X = fft(x);
X4 = fft(x4);
X12 = fft(x12);
X32 = fft(x32);

Mag = abs(X)/N;
Mag4 = abs(X4)/N4;
Mag12 = abs(X12)/N12;
Mag32 = abs(X32)/N32;

f = (0:N-1)*(Fs/N);
f4 = (0:N4-1)*(Fs4/N4);
f12 = (0:N12-1)*(Fs12/N12);
f32 = (0:N32-1)*(Fs32/N32);

f_adapted = f(1:(N/2)+1);
f4_adapted = f(1:(N4/2)+1);
f12_adapted = f(1:(N12/2)+1);
f32_adapted = f(1:(N32/2)+1);

Mag_adapted = Mag(1:(N/2)+1);
Mag4_adapted = Mag(1:(N4/2)+1);
Mag12_adapted = Mag(1:(N12/2)+1);
Mag32_adapted = Mag(1:(N32/2)+1);

%Mag_adapted(2:end -1) = 2 * Mag_adapted(2:end -1);
%figure(99);
%plot(f_adapted,Mag_adapted);
%stem(f_adapted,Mag_adapted);
%xlim([0,1600]);

figure(4);
subplot(4,1,1);
plot(f_adapted,Mag_adapted);
ylabel("Amplitude");
xlabel("frequencia");
title("original");
grid on;

subplot(4,1,2);
plot(f4_adapted,Mag4_adapted);
ylabel("Amplitude");
xlabel("frequencia");
title("400Hz");
grid on;

subplot(4,1,3);
plot(f12_adapted,Mag12_adapted);
ylabel("Amplitude");
xlabel("frequencia");
title("1200 Hz");
grid on;

subplot(4,1,4);
plot(f32_adapted,Mag32_adapted);
ylabel("Amplitude");
xlabel("frequencia Hz");
title("3200Hz");
grid on;

%4)

peaks1 =[];
freq_of_peaks = []
nPeaks = 0;
for i = 2:length(Mag_adapted)-1
  if Mag(i)> 0.01
    if Mag_adapted(i)> Mag_adapted(i-1) && Mag_adapted(i + 1) < Mag_adapted(i)
      peaks1 = [peaks1,Mag_adapted(i)];
      %freq_of_peaks = [freq_of_peaks,f_adabted(i)];
      nPeaks = nPeaks + 1;
    end
  end
end


printf("%d\n",peaks1);
printf("foram detetados %d picos",nPeaks);
printf("no(s) índice(s) %d, %d, %d \n",peaks1(1),peaks1(2),peaks1(3));
