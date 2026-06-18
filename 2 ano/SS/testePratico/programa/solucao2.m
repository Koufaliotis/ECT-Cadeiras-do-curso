% prob2.m
% Sampling theory demonstration for x(t) = cos(2π·800·t)

clear all; close all; clc;

%% Parameters
f_signal = 800;           % Signal frequency = 800 Hz
duration = 0.05;          % Duration = 0.05 seconds

%% 1. Generate original signal with high temporal resolution (20 kHz)
fs_high = 20000;          % High sampling frequency = 20 kHz
Ts_high = 1/fs_high;      % Sampling period
N_high = fs_high * duration;  % Number of samples (20000 * 0.05 = 1000)

t_high = (0:N_high-1) * Ts_high;  % Time vector
xa = cos(2 * pi * f_signal * t_high);  % Original signal

%% 2. Sample the signal at different frequencies
% Sampling frequencies
fs4 = 400;                % 400 Hz (BELOW Nyquist - aliasing expected!)
fs12 = 1200;              % 1200 Hz (ABOVE Nyquist - 2*800=1600? Actually below!)
fs32 = 3200;              % 3200 Hz (ABOVE Nyquist - good)

% Calculate sampling periods
Ts4 = 1/fs4;
Ts12 = 1/fs12;
Ts32 = 1/fs32;

% Number of samples for each
N4 = fs4 * duration;
N12 = fs12 * duration;
N32 = fs32 * duration;

% Time vectors for sampled signals
t4 = (0:N4-1) * Ts4;
t12 = (0:N12-1) * Ts12;
t32 = (0:N32-1) * Ts32;

% Sampled signals
x4 = cos(2 * pi * f_signal * t4);
x12 = cos(2 * pi * f_signal * t12);
x32 = cos(2 * pi * f_signal * t32);

%% 3. Plot original signal and sampled signals (time domain)
figure(1);

% Subplot 1: Original signal (xa)
subplot(4,1,1);
plot(t_high * 1000, xa, 'b-', 'LineWidth', 1);
xlabel('Tempo (ms)');
ylabel('Amplitude');
title('Sinal Original x_a(t) = cos(2π·800·t) - 20 kHz');
grid on;
xlim([0, duration * 1000]);

% Subplot 2: Sampled at 400 Hz (x4)
subplot(4,1,2);
stem(t4 * 1000, x4, 'r-', 'LineWidth', 1, 'MarkerSize', 4);
hold on;
plot(t_high * 1000, xa, 'b-', 'LineWidth', 0.5);  % Show original for reference
hold off;
xlabel('Tempo (ms)');
ylabel('Amplitude');
title('Sinal Amostrado x_4(t) - f_s = 400 Hz (abaixo de Nyquist)');
legend('Amostras', 'Sinal Original', 'Location', 'best');
grid on;
xlim([0, duration * 1000]);

% Subplot 3: Sampled at 1200 Hz (x12)
subplot(4,1,3);
stem(t12 * 1000, x12, 'g-', 'LineWidth', 1, 'MarkerSize', 4);
hold on;
plot(t_high * 1000, xa, 'b-', 'LineWidth', 0.5);
hold off;
xlabel('Tempo (ms)');
ylabel('Amplitude');
title('Sinal Amostrado x_{12}(t) - f_s = 1200 Hz (abaixo de Nyquist?)');
legend('Amostras', 'Sinal Original', 'Location', 'best');
grid on;
xlim([0, duration * 1000]);

% Subplot 4: Sampled at 3200 Hz (x32)
subplot(4,1,4);
stem(t32 * 1000, x32, 'm-', 'LineWidth', 1, 'MarkerSize', 4);
hold on;
plot(t_high * 1000, xa, 'b-', 'LineWidth', 0.5);
hold off;
xlabel('Tempo (ms)');
ylabel('Amplitude');
title('Sinal Amostrado x_{32}(t) - f_s = 3200 Hz (acima de Nyquist)');
legend('Amostras', 'Sinal Original', 'Location', 'best');
grid on;
xlim([0, duration * 1000]);

%% 4. Calculate and visualize spectrum using FFT

% Parameters for FFT
N_fft = 2048;  % For better frequency resolution

% Function to compute and plot spectrum
function [freqs, magnitude] = compute_spectrum(signal, fs, N_fft)
    X = fft(signal, N_fft);
    magnitude = abs(X) / length(signal);
    freqs = (0:N_fft-1) * (fs / N_fft);

    % One-sided spectrum
    magnitude = magnitude(1:N_fft/2+1);
    magnitude(2:end-1) = 2 * magnitude(2:end-1);
    freqs = freqs(1:N_fft/2+1);
end

% Compute spectra
[freqs_high, mag_high] = compute_spectrum(xa, fs_high, N_fft);
[freqs_4, mag_4] = compute_spectrum(x4, fs4, N_fft);
[freqs_12, mag_12] = compute_spectrum(x12, fs12, N_fft);
[freqs_32, mag_32] = compute_spectrum(x32, fs32, N_fft);

% Plot spectra
figure(2);

% Subplot 1: Original signal spectrum
subplot(4,1,1);
stem(freqs_high, mag_high, 'b-', 'LineWidth', 1, 'MarkerSize', 4);
xlabel('Frequência (Hz)');
ylabel('Magnitude');
title('Espectro do Sinal Original x_a(t) - f_s = 20 kHz');
grid on;
xlim([0, 2000]);

% Subplot 2: Spectrum of x4 (400 Hz sampling)
subplot(4,1,2);
stem(freqs_4, mag_4, 'r-', 'LineWidth', 1, 'MarkerSize', 4);
xlabel('Frequência (Hz)');
ylabel('Magnitude');
title('Espectro de x_4(t) - f_s = 400 Hz (Aliasing esperado)');
grid on;
xlim([0, 400]);

% Subplot 3: Spectrum of x12 (1200 Hz sampling)
subplot(4,1,3);
stem(freqs_12, mag_12, 'g-', 'LineWidth', 1, 'MarkerSize', 4);
xlabel('Frequência (Hz)');
ylabel('Magnitude');
title('Espectro de x_{12}(t) - f_s = 1200 Hz');
grid on;
xlim([0, 1200]);

% Subplot 4: Spectrum of x32 (3200 Hz sampling)
subplot(4,1,4);
stem(freqs_32, mag_32, 'm-', 'LineWidth', 1, 'MarkerSize', 4);
xlabel('Frequência (Hz)');
ylabel('Magnitude');
title('Espectro de x_{32}(t) - f_s = 3200 Hz');
grid on;
xlim([0, 3200]);

%% 5. Detect sinusoidal components in each signal

function [frequencies, magnitudes] = detect_peaks(freqs, mag, threshold)
    % Find peaks with magnitude above threshold
    peaks_idx = find(mag > threshold);

    % Group close frequencies (within 5 Hz)
    frequencies = [];
    magnitudes = [];

    for i = 1:length(peaks_idx)
        current_freq = freqs(peaks_idx(i));
        current_mag = mag(peaks_idx(i));

        % Check if this frequency is already detected
        is_duplicate = false;
        for j = 1:length(frequencies)
            if abs(current_freq - frequencies(j)) < 5
                is_duplicate = true;
                if current_mag > magnitudes(j)
                    magnitudes(j) = current_mag;
                end
                break;
            end
        end

        if ~is_duplicate
            frequencies = [frequencies, current_freq];
            magnitudes = [magnitudes, current_mag];
        end
    end

    % Sort by frequency
    [frequencies, idx] = sort(frequencies);
    magnitudes = magnitudes(idx);
end

% Detect peaks for each signal
threshold = 0.1;  % Magnitude threshold

[freqs_xa, mag_xa] = detect_peaks(freqs_high, mag_high, threshold);
[freqs_x4, mag_x4] = detect_peaks(freqs_4, mag_4, threshold);
[freqs_x12, mag_x12] = detect_peaks(freqs_12, mag_12, threshold);
[freqs_x32, mag_x32] = detect_peaks(freqs_32, mag_32, threshold);

% Print results
fprintf('\n========================================\n');
fprintf('ANÁLISE DE COMPONENTES ESPECTRAIS\n');
fprintf('========================================\n\n');

% Function to print formatted results
function print_results(signal_name, freqs, mags)
    n = length(freqs);
    if n == 0
        fprintf('O sinal %s contém 0 sinusoides\n', signal_name);
        fprintf('Não foram detectadas frequências significativas\n');
    elseif n == 1
        fprintf('O sinal %s contém %d sinusoide no índice 1\n', signal_name, n);
    else
        indices = sprintf('%d', 1);
        for i = 2:n-1
            indices = sprintf('%s, %d', indices, i);
        end
        if n > 1
            indices = sprintf('%s e %d', indices, n);
        end
        fprintf('O sinal %s contém %d sinusoide(s) nos índices %s\n', signal_name, n, indices);
    end

    if n > 0
        fprintf('As frequências presentes no sinal %s são: ', signal_name);
        for i = 1:n
            if i == n
                fprintf('%.1f Hz', freqs(i));
            elseif i == n-1
                fprintf('%.1f Hz e ', freqs(i));
            else
                fprintf('%.1f Hz, ', freqs(i));
            end
        end
        fprintf('\n');
    end
    fprintf('\n');
end

% Print results for each signal
print_results('xa', freqs_xa, mag_xa);
print_results('x4', freqs_x4, mag_x4);
print_results('x12', freqs_x12, mag_x12);
print_results('x32', freqs_x32, mag_x32);

%% 6. Theoretical analysis explanation
fprintf('========================================\n');
fprintf('ANÁLISE TEÓRICA\n');
fprintf('========================================\n');
fprintf('Sinal original: x(t) = cos(2π·800·t) → f = 800 Hz\n\n');
fprintf('Frequência de Nyquist: f_N = 2 × 800 = 1600 Hz\n\n');
fprintf('1) f_s = 400 Hz (ABAIXO de Nyquist):\n');
fprintf('   → Haverá ALIASING\n');
fprintf('   → 800 Hz será refletido para: f_aliased = |800 - 400| = 400 Hz\n');
fprintf('   → Também aparecerá em: 400 - 400 = 0 Hz (DC)\n\n');
fprintf('2) f_s = 1200 Hz (ABAIXO de Nyquist):\n');
fprintf('   → Ainda abaixo de 1600 Hz, portanto ALIASING\n');
fprintf('   → 800 Hz será refletido para: f_aliased = |1200 - 800| = 400 Hz\n');
fprintf('   → Também: 1200 - 400 = 800 Hz (original) e 1200 + 400 = 1600 Hz\n\n');
fprintf('3) f_s = 3200 Hz (ACIMA de Nyquist):\n');
fprintf('   → Sem aliasing, frequência correta: 800 Hz\n');
fprintf('   → Também aparecerá em: 3200 - 800 = 2400 Hz (imagem espelhada)\n');
fprintf('   → e em: 3200 + 800 = 4000 Hz\n');
