
import requests
import pandas as pd

class Searching:
    
    def search(self, url):
        r = requests.get(url)
         #extract the reaction
        response = r.json()
        results = response.get('results')
        
        if results is None or len(results) == 0:
            return None
        return results
    
    
    def search_generic_reaction(self, drug_name):
        '''
        This function takes a generic drug name and
        Returns a DataFrame on a succesful request for reactions
        Or returns None if no data is found
        '''
        url = f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.generic_name:"{drug_name.upper()}"&count=patient.reaction.reactionmeddrapt.exact'
        #make the request
        results = self.search(url)
        if results is None:
            return None
        
        reaction_list = []
        counting = []
        for result in results: 
            reaction_list.append(result['term'])
            counting.append(result['count'])
            
        df1 = pd.DataFrame({'reaction' : reaction_list, 'count' : counting})
        df1['percent'] = (df1['count'] / 
                  df1['count'].sum()) * 100
        df1 = df1.style.background_gradient()
        return df1
       
    def search_brand_reaction(self, drug_name):
        '''
        This function takes a brand drug name and
        Returns a DataFrame on a succesful request for reactions
        Or returns None if no data is found
        '''
        #formatting the url 
        url = f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.brand_name:"{drug_name.upper()}"&count=patient.reaction.reactionmeddrapt.exact'
        results = self.search(url)
        if results is None:
            return None
    
        df2 = pd.DataFrame(results, columns=['term', 'count'])
        df2['percent'] = (df2['count'] / 
                  df2['count'].sum()) * 100
        df2 = df2.style.background_gradient()
        return df2 

    def search_generic_indication(self, drug_name):
        '''
        This function takes a generic drug name and
        Returns a DataFrame on a succesful request for indication (aproved used)
        Or returns None if no data is found
        '''
        url = f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.generic_name:"{drug_name.upper()}"&count=patient.drug.drugindication.exact'
        results = self.search(url)
        if results is None:
            return None
    
        df3 = pd.DataFrame(results, columns=['term', 'count'])
        df3['percent'] = (df3['count'] / 
                  df3['count'].sum()) * 100
        df3 = df3.style.background_gradient()
        return df3 
    
    def search_brand_indication(self, drug_name):
        '''
        This function takes a brand drug name and
        Returns a DataFrame on a succesful request for indication (aproved used)
        Or returns None if no data is found
        '''
        #formatting the url 
        url = f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.brand_name:"{drug_name.upper()}"&count=patient.drug.drugindication.exact'
        results = self.search(url)
        if results is None:
            return None
    
        df4 = pd.DataFrame(results, columns=['term', 'count'])
        df4['percent'] = (df4['count'] / 
                  df4['count'].sum()) * 100
        df4 = df4.style.background_gradient()
        return df4 
    
    

    def search_generic_interaction(self, drug_name):
        '''
        This function takes in a generic name drug and
        returns a list of interactions with others drugs
        Or returns None if no data is found
        '''
        url = f'https://api.fda.gov/drug/label.json?search=openfda.generic_name:"{drug_name.upper()}"&search_after=drug_interaction'
        results = self.search(url)
        if results is None:
            return None
                
        interaction_list = []
        for result in results:
            interaction = result.get('drug_interactions')
            if interaction is not None:
                interaction_list.append(interaction)

        if len(interaction_list) == 0:        
            return None
        
        return interaction_list

    def search_brand_interaction(self, drug_name):
        '''
        This function takes in a brand name drug and
        returns a list of interactions with others drugs
        Or returns None if no data is found
        '''
        url = f'https://api.fda.gov/drug/label.json?search=openfda.brand_name:"{drug_name.upper()}"&search_after=drug_interaction'
        results = self.search(url)
        if results is None:
            return None
        
        interaction_list = []
        for result in results: 
            interaction = result.get('drug_interactions')
            if interaction is not None:
                interaction_list.append(interaction)
        
        if len(interaction_list) == 0:
            return None
        
        return interaction_list

#     type_name = input("Would you like to search for a generic name (generic) or brand name (brand)?")

#     drug_name = input(f"Please enter the {type_name} name.")

#     search_type = input ("Would you like to search for possible reactions (reaction) or interactions (interaction)")

#     if type_name == 'generic' and search_type == 'reaction':
#         print(search_generic_reaction(drug_name.upper()))
#     elif type_name == 'brand' and search_type == 'reaction':
#         print(search_brand_reaction(drug_name.upper()))
#     elif type_name == 'generic' and search_type == 'interaction': 
#         print(search_generic_interaction(drug_name.upper()))
#     elif type_name == 'brand' and search_type == 'interaction': 
#         print(search_brand_interaction(drug_name.upper()))


    
    