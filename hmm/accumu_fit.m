

%% fitting the ECDFs
single=fittype('1-exp(-k.*x)');
double = fittype('1 - a.*exp(-k1.*x)-(1-a).*exp(-k2.*x)');

options1 = fitoptions(single);
options1.Lower = 0;
options1.StartPoint = rand;

options2 = fitoptions(double); %setting lower and upper bounds for the floating variables
options2.Lower = [0 0 0]; 
options2.Upper = [1 Inf Inf];
options2.StartPoint = rand(1, 3); % this is between 0 and 1, but shouldn't bias too much.
n=6;
fit1=cell(n,1); % single exponential fits
gof1=cell(n,1);
fit2 = cell(n,1); %double exponential fits
gof2=cell(n,1);

for i = 1:n
    if length(t(i))>5 % need at least 5 observed lifetimes to try to fit it.
        [fit1{i}, gof1{i}] = fit(t(i), a(i), single, options1); %gof is "goodness of fit"
        [fit2{i}, gof2{i}] = fit(t(i), a(i), double, options2);
        %call the paramters by doing fit1(i).k1 etc
        
%% plotting the distributions (useful but not needed if not testing/making
        %figures)
            figure;
            plot(t(i), a(i), '.b');
            hold on
            plot(t(i), fit1{i}(t(i)), 'r');
            plot(t(i), fit2{i}(t(i)), 'g');
            set(gca, 'FontSize', 16, 'FontWeight', 'bold')
            xlabel('Lifetime (s)  ')
            ylabel('Cumulative Probability  ')
            title(['Cumulative distribution of lifetimes for state ', num2str(i), '   '])

%% plotting the distributions as linear fits. 
% could be useful for simplifying fit of single exp, but does not simplify fit of double exp
%             figure;
%             plot(t(i)(1:end-1), log(1-a(i)(1:end-1)), '.b');
%             set(gca, 'FontSize', 16, 'FontWeight', 'bold')
%             xlabel('Lifetime (s)  ')
%             ylabel('log of 1- Cumulative Probability  ')
%             title(['log of 1-Cumulative distribution of lifetimes for state ', num2str(i), '   '])
 
%% check if double exp.
        if gof1{i}.adjrsquare >= gof2{i}.adjrsquare
            result = ['Single exponential fit is better for state ', num2str(i)];
             disp(result)
            %        rates{i} = fit1{i}.k;
        else
            result = ['Double exponential fit is better for state ', num2str(i)];
             disp(result)
            doubleEx(i)=1;
            
%             figure; %show the plot to see how egregious the double exponential is.
%             plot(t(i), a(i), '.b');
%             hold on
%             plot(t(i), fit1{i}(t(i)), 'r');
%             plot(t(i), fit2{i}(t(i)), 'g');
%             set(gca, 'FontSize', 16, 'FontWeight', 'bold')
%             xlabel('Lifetime (s)  ')
%             ylabel('Cumulative Probability  ')
%             title(['Cumulative distribution of lifetimes for state ', num2str(i), '   '])

            %        rates{i} = [fit2{i}.a, fit2{i}.k1, fit2{i}.k2];
        end
        
        rates(i) = fit1{i}.k; % only want single exp fits right now, but still
        % leave in both fits to check that HMM is doing ok.
        CI(i, :) = confint(fit1{i}); %get the 95% confidence interval
        
    else
        rates(i) = 0; % if don't have 5 observed events, the event 
        % "doesn't happen" (or at least not often enough to quantify)
    end
end


