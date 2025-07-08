--AdderN
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity AdderN is
	generic( N : integer := 4);
	port(
	input0 : in std_logic_vector(N - 1 downto 0);
	input1 : in std_logic_vector(N - 1 downto 0);
	Cout : out std_logic;
	Sout : out std_logic_vector(N - 1 downto 0));
end AdderN;

architecture Behavioral of AdderN is

signal s_input0, s_input1, s_result : unsigned(N downto 0);

begin
		s_input0 <= '0' & unsigned(input0);
		s_input1 <= '0' & unsigned(input1);
		s_result <= s_input0 + s_input1;
		Sout <= std_logic_vector(s_result(N-1 downto 0));
		Cout <= std_logic(s_result(N));
end Behavioral;