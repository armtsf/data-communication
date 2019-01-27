function [c] = lloyd_quant(sigma, b)
infin = 1000;
n = 2000;
u_size = 2^b - 1;
c_size = 2^b;
c = zeros(c_size);

samples = normrnd(0, sigma, [1, n]);

u = (infin + infin) .* rand(u_size, 1) - infin;
u = sort(u);



for i = 1 : 5000
    for j = 1 : c_size
        if (j == 1)
            smptmp = samples(samples < u(j));
        elseif (j == c_size)
            smptmp = samples(samples > u(j - 1));
        else
            tmp = samples(samples < u(j));
            smptmp = tmp(tmp > u(j - 1));
        end
        min = inf;
        if (size(smptmp) == 0)
            if (j == 1)
                c(j) = (-infin + u(j)) / 2;
            elseif (j == c_size)
                c(j) = (infin + u(j)) / 2;
            else
                c(j) = (u(j) + u(j + 1)) / 2;
            end
        else
            for x = smptmp
                summ = sum(arrayfun(@(y) ((y - x)^2), smptmp));
                if (summ < min)
                    min = summ;
                    c(j) = x;
                end
            end
        end
    end
    for k = 1 : u_size
        u(k) = (c(k) + c(k+1)) / 2;
    end
end
end