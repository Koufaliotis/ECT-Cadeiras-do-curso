% prob1.m
% Signal analysis script for x(t) = 2cos(150πt) + sin(300πt) + 0.5cos(450πt)

clear all; close all; clc;

%% 1. Create signal vector with sampling rate of 10 kHz for 0.1 seconds
fs = 10000;           % Sampling frequency = 10 kHz
Ts = 1/fs;            % Sampling period
duration = 0.1;       % Duration in seconds
N = fs * duration;    % Number of samples (10000 * 0.1 = 1000 samples)

t = (0:N-1) * Ts;     % Time vector

% Generate the signal: x(t) = 2cos(150πt) + sin(300πt) + 0.5cos(450πt)
% Using: cos(2πf t) = cos(ω t) where ω = 150π → 2πf = 150π → f = 75 Hz
% Similarly: sin(300πt) → sin(2π·150·t) → f = 150 Hz
% cos(450πt) → f = 225 Hz

x = 2 * cos(150 * pi * t) + sin(300 * pi * t) + 0.5 * cos(450 * pi * t);

%% 2. Plot the signal
figure(1);
plot(t, x, 'b-', 'LineWidth', 1);
xlabel('Time (s)');
ylabel('Amplitude');
title('Signal x(t) = 2cos(150πt) + sin(300πt) + 0.5cos(450πt)');
grid on;
xlim([0, 0.02]);  % Show first 20 ms for better visualization

%% 3. Calculate and display magnitude spectrum using FFT
% Compute FFT
X = fft(x);
% Compute two-sided magnitude spectrum
magnitude = abs(X) / N;  % Normalize by number of samples
% Create frequency vector for two-sided spectrum
frequencies = (0:N-1) * (fs / N);

% Plot one-sided spectrum (more common for real signals)
figure(2);
% One-sided spectrum: take first half of frequencies
one_sided_mag = magnitude(1:N/2+1);
one_sided_mag(2:end-1) = 2 * one_sided_mag(2:end-1);  % Account for negative frequencies
freq_one_sided = frequencies(1:N/2+1);

stem(freq_one_sided, one_sided_mag, 'r', 'LineWidth', 1.5, 'MarkerSize', 8);
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Magnitude Spectrum of x(t)');
grid on;
xlim([0, 300]);  % Focus on relevant frequency range (0-300 Hz)

%% 4. Find sinusoidal components (peaks in spectrum)
% Detect peaks (frequencies with significant magnitude)
tolerance = 1;  % Hz tolerance for detection
peaks = [];
peak_indices = [];

for k = 1:length(freq_one_sided)
    if one_sided_mag(k) > 0.01  % Threshold to ignore numerical noise
        peaks = [peaks, one_sided_mag(k)];
        peak_indices = [peak_indices, k];
    end
end

% Remove duplicate peaks due to DFT frequency resolution
detected_freqs = [];
detected_mags = [];

for i = 1:length(peak_indices)
    current_freq = freq_one_sided(peak_indices(i));
    current_mag = one_sided_mag(peak_indices(i));

    % Check if this frequency is already detected (within tolerance)
    is_duplicate = false;
    for j = 1:length(detected_freqs)
        if abs(current_freq - detected_freqs(j)) < tolerance
            is_duplicate = true;
            % Keep the one with higher magnitude
            if current_mag > detected_mags(j)
                detected_freqs(j) = current_freq;
                detected_mags(j) = current_mag;
            end
            break;
        end
    end

    if ~is_duplicate
        detected_freqs = [detected_freqs, current_freq];
        detected_mags = [detected_mags, current_mag];
    end
end

% Sort by frequency
[detected_freqs, sort_idx] = sort(detected_freqs);
detected_mags = detected_mags(sort_idx);

%% 5. Display results
n = length(detected_freqs);
% Format indices message
if n == 1
    indices_msg = sprintf('indice %d', 1);
elseif n == 2
    indices_msg = sprintf('indices %d e %d', 1, 2);
else
    indices_msg = sprintf('indices 1, 2 e 3');
end

fprintf('O sinal contém %d sinusoide(s) nos %s\n', n, indices_msg);

% Format frequencies message
freq_str = '';
for i = 1:n
    if i == n
        freq_str = sprintf('%s%.1f Hz', freq_str, detected_freqs(i));
    elseif i == n-1 && n > 1
        freq_str = sprintf('%s%.1f Hz e ', freq_str, detected_freqs(i));
    else
        freq_str = sprintf('%s%.1f Hz, ', freq_str, detected_freqs(i));
    end
end
fprintf('As frequências presentes no sinal são: %s\n', freq_str);

%% 6. Additional verification: Theoretical frequencies
fprintf('\n--- Verification ---\n');
fprintf('Theoretical frequencies:\n');
fprintf('Component 1: 2cos(150πt) → frequency = 75 Hz\n');
fprintf('Component 2: sin(300πt) → frequency = 150 Hz\n');
fprintf('Component 3: 0.5cos(450πt) → frequency = 225 Hz\n');

%% 7. Print FFT resolution
freq_resolution = fs / N;
fprintf('\nFFT frequency resolution: %.2f Hz\n', freq_resolution);

%% Optional: Zoomed spectrum for better visualization
figure(3);
stem(freq_one_sided, one_sided_mag, 'r', 'LineWidth', 1.5, 'MarkerSize', 8);
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Magnitude Spectrum (Zoomed)');
grid on;
xlim([50, 250]);
ylim([0, 1.2]);

% Add text annotations for the peaks
hold on;
for i = 1:length(detected_freqs)
    plot(detected_freqs(i), detected_mags(i), 'bo', 'MarkerSize', 10, 'LineWidth', 2);
    text(detected_freqs(i), detected_mags(i) + 0.05, ...
         sprintf('%.1f Hz', detected_freqs(i)), ...
         'HorizontalAlignment', 'center', 'FontSize', 10);
end
hold off;

%% Display peak information
fprintf('\n--- Detected Peaks ---\n');
for i = 1:length(detected_freqs)
    fprintf('Peak %d: %.2f Hz (magnitude = %.3f)\n', ...
            i, detected_freqs(i), detected_mags(i));
end
