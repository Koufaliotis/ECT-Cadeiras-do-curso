library IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

entity ShiftRegN is
generic (size : positive := 4);

	port(
		clock : in std_logic;
		loadEn : in std_logic;
		dataIn : in std_logic_vector(size -1 downto 0);
		dirLeft : in std_logic;
		dataOut : out std_logic_vector(size -1 downto 0));
end ShiftRegN;

architecture Behavioral of ShiftRegN is
signal s_shiftReg : std_logic_vector(size -1 downto 0);
begin
	process(clock)
	begin
	if (rising_edge(clock)) then
		if (loadEn = '1') then
			s_shiftReg <= dataIn;
		elsif (dirLeft = '1') then
			s_shiftReg <= s_shiftReg(size -2 downto 0) & '0';--???? left pull
		--else
			--s_shiftReg <= '0' & s_shiftReg(size-1 downto 1); --exmp 1011 => 0101 right pull
		end if;
	end if;
	end process;

dataOut <= s_shiftReg;
end Behavioral;