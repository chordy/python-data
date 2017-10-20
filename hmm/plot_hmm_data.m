close all

%% plot rawdata, filtered data, hidden states
l1=length(rawdata);
l2=length(hidden_means);
x1=1:l1;
x1=(x1-1)*0.4;
x2=1:l2;
x2=(x2-1)*2;
start=4001;
stp=4500;
figure;
hold all
% scatter(x1(start:stp*5)/1000,rawdata(start:stp*5),10,'.','MarkerEdgeColor',[0.5 .5 .5],...
%               'MarkerFaceColor',[0.5 .5 .5],...
%               'LineWidth',1);
plot(x2(start:stp)/1000,filtered_data(start:stp),'b');
plot(x2(start:stp)/1000,hidden_means(start:stp),'Color',[1,0.5,0]);
set(gca, 'FontSize', 16, 'FontWeight', 'bold')
ylim([5.5 9]);
xlabel('Time (s)  ')
ylabel('Force(pN) ')
hold off

%% plot state distribution
% 
% figure;
% hold all
% for i=1:length(mu)
%     x_range=[mu(i)-5*sigma(i):0.1*sigma(i):mu(i)+5*sigma(i)];
%     norm=sum(life{i})*normpdf(x_range,mu(i),sigma(i));
%     plot(x_range,norm,'LineWidth',1)
%     xlim([min(mu)-0.2*(max(mu)-min(mu)) max(mu)+0.2*(max(mu)-min(mu)) ]);
% end
% [exten, forc]=ef_cal(filtered_data,filtered_ext,hidden_states);
% c=abs(pcontour(exten,mu))
% % % figure;
% % % plot(exten)
% % figure;
% % plot(forc)
