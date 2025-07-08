library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
USE iEEE.NUMERIC_STD.ALL;

entity FreqDivider_Demo is 
			port(CLOCK_50 : IN STD_LOGIC;
				  SW : IN STD_LOGIC_VECTOR(0 DOWNTO 0);
				  CLOCK_OUT : OUT STD_LOGIC);
END FreqDivider_Demo;



architecture Structural of FreqDivider_Demo is
constant x : std_logic_vector(31 downto 0) := x"02FAF080";
	begin
		divisor: entity work.FreqDivider(Behavioral)
							port map(
										clkIn => CLOCK_50,
										reset => SW(0), 
										clkOut => CLOCK_OUT,
										k => x );
	
	end Structural;