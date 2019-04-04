traffic_light = imread('whole_amber_traffic_light.png');
[x,y,z] = size(traffic_light);
total_pixels = x*y;

red_values = 1: total_pixels;
green_values = 1: total_pixels;
blue_values = 1: total_pixels;
k=1;

for i=1:x
for j=1:y
red_values(k) = traffic_light(i,j,1);
green_values(k) = traffic_light(i,j,2);
blue_values(k) = traffic_light(i,j,3);
k=k+1;
end
end

r=mean(red_values);
g=mean(green_values);
b=mean(blue_values);

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
