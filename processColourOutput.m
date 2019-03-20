r = 69;
g = 248;
b = 66;

fis = readfis('Fuzzy_RGB');
out = evalfis([r g b], fis);

if (out > 0.625 && out < 2.25)
    colour = 'green'
elseif (out >= 2.25 && out < 3.75)
    colour = 'yellow / amber'
elseif (out >= 3.75)
    colour = 'red'
else 
    colour = 'none'
end