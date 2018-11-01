PACKAGE CONTENTS  
​    <a href="#1"> async_build_markets   </a>  
​    <a href="#2"> async_find_opportunities   </a>  
​   <a href="#3"> bellman_multi_graph  </a>  
​   <a href="#4"> bellmannx </a>  
​   <a href="#5"> outliers </a>  
​   <a href="#6"> tests (package) </a>  
​   <a href="#7">utils (package) </a>  
SUBMODULES  
​    data_structures  
​    drawing  
​    general  
​    graph_utils  
​    misc  
​    multi_exchange  
​    single_exchange  
DATA  
​    accepted_types = {<class 'networkx.classes.multidigraph.MultiDiGraph'>...   

# <a name="1"> async_build_mark </a>
## class CollectionBuilder:
```python
def __init__(self):
async def async_build_all_collections(self, write=True, ccxt_errors=False, collections_dir='./'):
def build_all_collections(self, write=True, ccxt_errors=False, collections_dir='./'):
async def _add_exchange_to_collections(self, exchange_name: str, ccxt_errors=False):
```
## class SpecificCollectionBuilder(CollectionBuilder):
```python
def __init__(self, blacklist=False, **kwargs):
async def _add_exchange_to_collections(self, exchange_name: str, ccxt_errors=False):
def _check_exchange_meets_criteria(self, exchange):
def _element_of_type_in_list(self, element, actual_value_type, actual_value, key):
```
## class ExchangeMultiGraphBuilder:
```python
def __init__(self, exchanges: list):
def build_multi_graph(self, write=False, ccxt_errors=False):
async def _add_exchange_to_graph(self, exchange_name: str, ccxt_errors=False):
```
## def build_multi_graph_for_exchanges(exchanges: list):
## def build_arbitrage_graph_for_exchanges(exchanges: list, k_core=2):
## def build_collections(blacklist=False, write=True, ccxt_errors=False):
## async def async_build_specific_collections(blacklist=False, write=False, ccxt_errors=False, **kwargs):
## def build_specific_collections(blacklist=False, write=False, ccxt_errors=False, **kwargs):
## async def async_build_all_collections(write=True, ccxt_errors=False):
## def build_all_collections(write=True, ccxt_errors=False):
## async def async_get_exchanges_for_market(symbol, collections_dir='./'):
## def get_exchanges_for_market(symbol, collections_dir='./'):
# <a name="2"> async_find_opportunities </a>
## class OpportunityFinder:
```python
def __init__(self, market_name, exchanges=None, name=True):
async def _test_bid_and_ask(self, exchange):
async def find_min_max(self):
```
## async def get_opportunity_for_market(symbol, collections_dir, exchanges=None, name=True):

# <a name="3"> bellman_multi_graph </a>
## class NegativeWeightFinderMulti(NegativeWeightFinder):
```python
def __init__(self, graph: nx.MultiGraph):
def bellman_ford(self, source, loop_from_source=True, ensure_profit=False, unique_paths=False):
def _first_iteration(self):
def _process_edge_bunch(self, edge_bunch):
```
## def bellman_ford_multi(graph: nx.MultiGraph, source, loop_from_source=False, ensure_profit=False, unique_paths=False):

# <a name="4"> bellmannx </a>
## class NegativeWeightFinder:
```python
def __init__(self, graph: nx.Graph, depth=False, starting_amount=1):
def _set_basic_fields(self, node):
def initialize(self, source):
def bellman_ford(self, source, loop_from_source=False, ensure_profit=False, unique_paths=True):
def _check_final_condition(self, **kwargs):
def relax(self, edge):
def _retrace_negative_loop(self, start, loop_from_source=False, source='', ensure_profit=False, unique_paths=False):
def reset_predecessor_iteration(self):
```
## class NegativeWeightDepthFinder(NegativeWeightFinder):
```python
def __init__(self, graph: nx.Graph):
def initialize(self, source):
def relax(self, edge):
def _check_final_condition(self, **kwargs):
```
## def bellman_ford(graph, source, loop_from_source=False, ensure_profit=False, unique_paths=False, depth=False,starting_amount=1):
## def calculate_profit_ratio_for_path(graph, path, depth=False, starting_amount=1):

# utils(package)
```python
from .drawing import *
from .general import ExchangeNotInCollectionsError, print_profit_opportunity_for_path,  print_profit_opportunity_for_path_multi
from .multi_exchange import create_multi_exchange_graph, create_weighted_multi_exchange_digraph,multi_graph_to_log_graph
from .single_exchange import load_exchange_graph, create_exchange_graph, populate_exchange_graph
from .misc import last_index_in_list, next_to_each_other
from .data_structures import StackSet, PrioritySet
from .graph_utils import get_greatest_edge_in_bunch, get_least_edge_in_bunch
```
# drawing
## def draw_graph_to_png(graph, to_file: str):
## def format_graph_for_json(graph, raise_errors=True):
## def write_graph_to_json(graph, to_file: str, raise_errors=True):
## def multi_digraph_from_json(file_name: str):
## def digraph_from_dict(data):
## def multi_digraph_from_dict(data):
# general
## class ExchangeNotInCollectionsError(Exception):
```python
def __init__(self, market_ticker):
```
## def print_profit_opportunity_for_path(graph, path, round_to=None, depth=False, starting_amount=100):
## def print_profit_opportunity_for_path_multi(graph: nx.Graph, path, print_output=True, round_to=None, shorten=False):

# multi_exchange
## def create_multi_exchange_graph(exchanges: list, digraph=False):
## def create_weighted_multi_exchange_digraph(exchanges: list, name=True, log=False, fees=False, suppress=None):
## async def _add_exchange_to_multi_digraph(graph: nx.MultiDiGraph, exchange, log=True, suppress=None):
## async def _add_market_to_multi_digraph(exchange, market_name: str, graph: nx.DiGraph, log=True, suppress=None):
## def multi_graph_to_log_graph(digraph: nx.MultiDiGraph):

# single_exchange
## def create_exchange_graph(exchange: ccxt.Exchange):
## async def load_exchange_graph(exchange, name=True, fees=False, suppress=None, depth=False) -> nx.DiGraph:
## async def populate_exchange_graph(graph: nx.Graph, exchange: ccxt.Exchange, log=True, fees=False, suppress=None) -> nx.DiGraph:
## async def _add_weighted_edge_to_graph(exchange: ccxt.Exchange, market_name: str, graph: nx.DiGraph, log=True, fee=0, suppress=None, ticker=None, depth=False):

# misc
## def next_to_each_other(li: list, *args):
## def last_index_in_list(li: list, element):

# data_structures
## class StackSet:
```python
def __init__(self):
def add(self, element, enforce_stack=True):
def peek(self):
def pop(self):
def soft_pop(self):
@property
def done_popping(self):
def __len__(self):
def __repr__(self):
def __str__(self):
```
## class PrioritySet:
```python
def __init__(self):
def add(self, d, pri):
def pop(self):
def peek(self):
def reset(self):
@property
def empty(self):
def __str__(self):
def __repr__(self):
def __len__(self):
```
## graph_utils
## def get_greatest_edge_in_bunch(edge_bunch, weight='weight'):
