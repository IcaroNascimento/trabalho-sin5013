#include <bits/stdc++.h>
using namespace std;

int f, n;
bool positivo[50], negativo[50];
int entrada[50];
map<pair<int,int>, bool> memo;

bool resolvedor(int id, int soma){

    if(id >= n && soma == f) return true;
    else if (id>=n) return false;
    if(memo.count(make_pair(soma,id))!=0) return memo[make_pair(soma,id)];

    bool ent = false, saida = false;

    ent = resolvedor(id + 1, soma+entrada[id]);
    saida = resolvedor(id + 1, soma-entrada[id]);

    if(ent  &&  !saida) positivo[id] = true;
    else if(!ent && saida) negativo[id] = true;
    else if(ent && saida) positivo[id] = negativo[id] = true;
    return memo[make_pair(soma,id) ] = (ent || saida) ? true:false;
}

int main(){
    while(scanf("%d %d", &n, &f)  && n>0){
        
        memo.clear();
        for (int i=0; i<n; i++){
            positivo[i] = negativo[i] = false;
            scanf("%d", &entrada[i]);
        }
        bool valido = resolvedor(0,0);
        
        for (int i=0; i<n && valido; i++){
            if(positivo[i] && negativo[i]) printf("?");
            else if(positivo[i]) printf("+");
            else printf("-");
        }
        if(!valido) printf("*");
        printf("\n");
    }
    return (0);
}
