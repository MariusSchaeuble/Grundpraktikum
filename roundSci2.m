function res = roundSci2(messwert, fehler)
if fehler == 0
    disp("fehler von 0, macht keinen sinn")
    return;
end
%eingabe in gleichen einheiten, als num 
%messwertStr = num2str(messwert);
fehlerStr = num2str(fehler);
%ermittle rundefaktor k
k = -127;
p = strfind(fehlerStr, ".");
if ~isempty(p)
    for i=1:strlength(fehlerStr)
        if extract(fehlerStr, i) =="3" || extract(fehlerStr, i) =="4" || extract(fehlerStr, i) =="5" || extract(fehlerStr, i) =="6" || extract(fehlerStr, i) =="7" || extract(fehlerStr, i) =="8" || extract(fehlerStr, i) =="9"
            if i < p(1)
                k = i - p(1) + 1;
                %display(k);
            else
                k = i - p(1);
                %display(k);
            end
            break;
        end
        if (extract(fehlerStr, i) == "1") || (extract(fehlerStr, i) == "2")
                if i+1 < p(1)
                        k = i - p(1) + 2;
                        %display(k);
                else
                        k = i - p(1) +1;
                        %display(k);
                        if k == 0
                            k = 1;
                        end
                end
                break;
        end %fall 1 | 2
    end
    e = strfind(fehlerStr, "e");
    if ~isempty(e)
        k = k - str2num(substringIncl(fehlerStr, e+1, strlength(fehlerStr)));
    end
else
    %kein komma
    e = strfind(fehlerStr, "e");
    if isempty(e)
        for i=1:strlength(fehlerStr)
            if extract(fehlerStr, i) =="3" || extract(fehlerStr, i) =="4" || extract(fehlerStr, i) =="5" || extract(fehlerStr, i) =="6" || extract(fehlerStr, i) =="7" || extract(fehlerStr, i) =="8" || extract(fehlerStr, i) =="9"
                k = i - strlength(fehlerStr);
                %display(k);
                break;
            end
            if extract(fehlerStr, i) =="1" || extract(fehlerStr, i) =="2"
                k = i - strlength(fehlerStr) + 1;
                %display(k);
                break;
            end
        end
    else
        for i=1:e
            if extract(fehlerStr, i) =="3" || extract(fehlerStr, i) =="4" || extract(fehlerStr, i) =="5" || extract(fehlerStr, i) =="6" || extract(fehlerStr, i) =="7" || extract(fehlerStr, i) =="8" || extract(fehlerStr, i) =="9"
                k = i - e + 1;
                %display(k);
                break;
            end
            if extract(fehlerStr, i) =="1" || extract(fehlerStr, i) =="2"
                k = i - e + 2;
                %display(k);
                break;
            end
        end
        k = k - str2num(substringIncl(fehlerStr, e+1, strlength(fehlerStr)));
    end % fall e ex.
end
%eigentliches runden
fehler = (10^k)*fehler;
fehler = roundUP(fehler);
fehler = fehler/(10^k); 
messwert = (10^k)*messwert;
messwert = round(messwert);
messwert = messwert/(10^k);

%auf die passende länge angeben
fehler = sprintf("%." + num2str(max([0, k])) + "f",fehler);
messwert = sprintf("%." + num2str(max([0, k])) + "f",messwert);
res = [messwert; fehler; k];



end