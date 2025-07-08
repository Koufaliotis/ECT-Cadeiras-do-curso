LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY DrinksMachine IS
    port(clock : in std_logic;
         reset : in std_logic;
         V : in std_logic;
         C : in std_logic;
         drink : out std_logic);
end DrinksMachine;

architecture Behavioral of DrinksMachine IS
    type TState is (E0,E1,E2,E3,E4,E5);
    signal pState, nState : TState;

begin
		sync_proc : process(clock)
		begin
			if (rising_edge(clock)) then
				if (reset = '1') then
					pState <=E0;
				else
					pState <= nState;
				end if;
			end if;
		
		end process;
		comb_proc : process(pState, V, C)
			begin
				case (pState) is

					when E0 =>
								drink <= '0'; --Moore Output
								if (V = '1' and C='0') then
									nState <= E1;
								elsif (V = '0' and C='1') then
									nState <= E3;
								else
									nState <= E0;
								end if;

					when E1 =>
								drink <= '0';--?????????????????????????????????????/
								if (V = '1' and C='0') then
									nState <= E2;
								elsif (V = '0' and C='1') then
									nState <= E4;
								else
									nState <= E1;
								end if;
								
									
					when E2 =>
								drink <= '0';--?????????????????????????????????????/
								if (V = '1' and C='0') then
									nState <= E3;
								elsif (V = '0' and C='1') then
									nState <= E5;
								else
									nState <= E2;
								end if;
					
					when E3 =>
								drink <= '0';--?????????????????????????????????????/
								if (V = '1' and C='0') then
									nState <= E4;
								elsif (V = '0' and C='1') then
									nState <= E5;
								else
									nState <= E3;
								end if;
					
					when E4 =>
								drink <= '0';--?????????????????????????????????????/
								if (V = '1' or C='1') then
									nState <= E5;
								else
									nState <= E4;
								end if;
					when E5 =>
								drink <= '1';--?????????????????????????????????????/
								nstate <= E0;
				end case;
			end process;
end Behavioral;