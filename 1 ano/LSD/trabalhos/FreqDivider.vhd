library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
USE iEEE.NUMERIC_STD.ALL;


entity FreqDivider is 
   port(clkIn  : in  std_logic; --????
		  reset : in std_logic; --to restart the clock 
		  k : in std_logic_vector(31 downto 0); --???
        clkOut : out std_logic); --???
end FreqDivider; 
 
architecture Behavioral of FreqDivider is 
   signal s_counter : unsigned(31 downto 0);
	--signal s_counter : natural; --natural numbers???? yes
   signal s_halfWay ,s_final: unsigned(31 downto 0);   
begin 
   s_halfWay <= (unsigned(k) / 2); 
	s_final <= unsigned(k);
	
   process(clkIn) 
   begin 
      if (rising_edge(clkIn)) then 
		--contineu here -- for the clock loop (-1 to not goa above the s_final)
			if (reset = '1' or s_counter = s_final - 1) then  -- <--error here
				clkOut <= '0';
				s_counter <= (others => '0');
				--s_counter <= 0;
			else
			--start counting seconds????????
				if (s_counter = s_halfWay) then --is counter the clock or the seconds
					clkOut <= '1';
					
				end if;
				s_counter <= s_counter + 1;
				
			end if;	
 
      end if; 
   end process; 
end Behavioral;