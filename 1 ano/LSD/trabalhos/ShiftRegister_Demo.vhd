--ShiftRegister_Demo
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

entity ShiftRegister_Demo is
	port(
			CLOCK_50 : in std_logic;
			loadEn : in std_logic;
			SW : in std_logic_vector(9 downto 0);
			clkOut : out std_logic;
			LEDR : out std_logic_vector(7 downto 0)
			);
			
end ShiftRegister_Demo;

architecture stracture of ShiftRegister_Demo is
signal s_out : std_logic_vector(7 downto 0);
signal s_clock : std_logic; 
begin		
		shifter : entity work.ShiftRegN(Behavioral)
		generic map(
            size => 8
        )
		
		port map(
					dataIn => SW(7 downto 0),
					clock => s_clock,
					dirLeft => SW(8),
					loadEn => SW(9),
					dataOut => s_out);
					
		
		clock : entity work.ClkDividerN(Behavioral)
		
			generic map(
						divFactor =>50000000) --in Hz
						--como ligar o pulso??
			port map(
						clkIn => CLOCK_50,      
						clkOut => s_clock    
						);
			LEDR <= s_out;
end stracture;