-- .\lua54 main.lua

--function int(str)
--    return tonumber(str)
--end
--
--print("Please enter your age:")
--local age = int(io.read())
--
--if age < 21 then
--    print("You are not of age to drink. You have " .. 21 - age .. " years until you can.")
--elseif age >= 21 then
--    print("You can drink.")
--end

-- creates sleep function
local clock = os.clock
function sleep(n)  -- seconds
   local t0 = clock()
   while clock() - t0 <= n do
   end
end

-- creates input function
function input(state)
    print(state)
    return io.read()
end

print(" _______    _______    ___        ______             __   __    ___     __    _    _______  ")
sleep(1)
print("|       |  |       |  |   |      |      |           |  |_|  |  |   |   |  |  | |  |       |")
sleep(1)
print("|    ___|  |   _   |  |   |      |  _    |          |       |  |   |   |   |_| |  |    ___|")
sleep(1)
print("|   | __   |  | |  |  |   |      | | |   |          |       |  |   |   |       |  |   |___ ")
sleep(1)
print("|   ||  |  |  |_|  |  |   |___   | |_|   |          | ||_|| |  |   |   |  _    |  |    ___|")
sleep(1)
print("|   |_| |  |       |  |       |  |       |          | |   | |  |   |   | | |   |  |   |___ ")
sleep(1)
print("|_______|  |_______|  |_______|  |______|           |_|   |_|  |___|   |_|  |__|  |_______|")
sleep(0.5)

print("\nWELCOME TO THE GOLD MINE!")

gold = 0
running = true

while running do

    print("--If you want to check your amount of Gold, enter 1")
    print("--If you want to enter the GOLD MINE, enter 2")
    path1 = input("--If you want to gamble your Gold, enter 3")

    if path1 == "quit" then
        running = false
    end

    if path1 == "1" then
        print("\nYou have: " .. gold .. " gold.\n\n")
    elseif path1 == "2" then
        print("\nThe cold, dark hollows of the Gold Mine beckon for a payday!\n")

        if gold < 0 then
            sleep(0.5)
            gold = gold + 25
            print("It seems that you've indebted your Gold, here's 25 to get you out.\n\n+25 Gold\nNew Balance: " .. gold .. ".\n")

        else

            sleep(0.5)

            local ore_size = math.random(1, 100)
            if ore_size >= 25 then
                
                print("Your pickaxe strikes a Small Ore")
                sleep(1.5)
                plunder = math.random(-15, 15)
                if plunder <= 0 then
                    plunder = 0
                end
                gold = gold + plunder
                if plunder == 0 then

                    print("\nThe ore contained no Gold.\n")
                    print("New Balance: " .. gold .. ".\n")
                    sleep(1.5)

                else
                    print("\nYou acquired " .. plunder .. " gold!\n+" .. plunder .. " Gold\nNew Balance: " .. gold .. ".\n")
                    sleep(1.5)
                end

            elseif ore_size <= 25 and ore_size >=6 then

                print("Your pickaxe strikes a Medium Ore")
                sleep(1.5)
                plunder = math.random(50, 80)
                gold = gold + plunder

                print("\nYou acquired " .. plunder .. " gold\n+" .. plunder .. " Gold\nNew Balance: " .. gold .. ".\n")
                sleep(1.5)
            
            elseif ore_size <= 5 then

                print("Your pickaxe strikes a Large Ore")
                sleep(1.5)
                plunder = math.random(81, 120)

                gold = gold + plunder

                print("\nYou acquired " .. plunder .. " gold\n+" .. plunder .. " Gold\nNew Balance: " .. gold .. ".\n")
                sleep(1.5)

            end
        end

    elseif path1 == "3" then

        while true do
            gamamnt = tonumber(input("How much of yer Gold would you like to raise?\nCurrent Balance: " .. gold .. ".\n"))
            if gamamnt > gold or gamamnt < 0 then
                print("That value is illegal")
            else
                break
            end
        end

        print("Alright, the dice are rolling!\n")
        old_balance = gold
        sleep(1.5)
        factor = math.random(1, 10)
        if factor >= 3 then
            gold = gold - math.ceil((gamamnt / math.random(2, 5)))
            print("Unfavored. You lost " .. old_balance - gold .. " gold.\n\nNew Balance: " .. gold .. ".\n")
        else

            gold = gold * math.random(2, 4)
            print("Favored! You gained " .. gold - old_balance .. " gold.\n\nNew Balance: " .. gold .. ".\n")

        end

    elseif path1 == "gmod" then

        k = tonumber(input("new value:"))
        if k == "reset" then
            gold = 0
        else
            gold = k
        end
    end
end