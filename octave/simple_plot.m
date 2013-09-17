x=linspace(1,100,10000);
  for i=1:numel(x)
	  y(i) = log(x(i));
  end

plot(x,y)
