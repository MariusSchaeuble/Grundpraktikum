function res = gauss(term, strings, stringvalues, errors, singlevaluesStrings, singlevalues)
if (length(strings) ~= length(stringvalues) || length(strings) ~= length(errors) || length(stringvalues) ~= length(errors) || length(singlevaluesStrings) ~= length(singlevalues))
    res = -127;
    return;
end
h1 = size(strings);
h2 = size(singlevalues);
l1 = h1(2);
l2 = h2(2);
derivatives = zeros(l1, 1);
str = "";
for i=1:l1
    str = "eval(diff(" + term + ", " + strings(i) + "),{ ";
    for j=1:l1-1
        str = str + strings(j) + "=" + num2str(stringvalues(j)) + ",";
    end
    str = str + strings(l1) + "=" + num2str(stringvalues(l1));
    for j=1:l2
        str = str + ", " + singlevaluesStrings(j) + "=" + singlevalues(j);
    end
    str = str + "})";
    derivatives(i) = double(maple(str));
end
res = 0;
for i=1:l1
    res = res + (derivatives(i)*errors(i))^2;
end
res = sqrt(res);
return;
end