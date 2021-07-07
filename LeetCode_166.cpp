class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
		long numer = (long)abs(numerator);
		long denom = (long)abs(denominator);
		int temp=0,start=-1;
		bool minus=false;
		vector<int> recurr;
		unordered_map<int,int> visited;
		string ans = "";
    	if(numerator==0) return "0";
		if((numerator>0 && denominator<0) || (numerator<0 && denominator>0))
			ans+="-";
		ans+=to_string(numer/denom);
		numer%=denom;
		while(numer){
			long quotient = numer*10/denom;
			if(!visited.empty() && visited.find(numer)!=visited.end()){
				start=visited.find(numer)->second;
				break;
			}
			recurr.push_back((int)quotient);
			visited.insert(make_pair(numer,temp));
			numer = (numer*10)%denom;
			temp++;
		}
		if(!recurr.empty()){
			ans+=".";
			if(start==-1){
				for(int i=0; i<recurr.size(); ++i)
					ans+=to_string(recurr[i]);
			}
			else{
				for(int i=0; i<start; ++i)
					ans+=to_string(recurr[i]);
				if(start!=-1) ans+="(";
				for(int i=start; i<recurr.size(); ++i)
					ans+=to_string(recurr[i]);
				if(start!=-1) ans+=")";
			}
		}
		
		return ans;
    }
};