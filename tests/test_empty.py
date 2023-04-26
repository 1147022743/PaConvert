
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../')

import textwrap

from tests.apibase import APIBase

class EmptyAPI(APIBase):

    def __init__(self, pytorch_api) -> None:
        super().__init__(pytorch_api)

    def check(self, pytorch_result, paddle_result):
        if pytorch_result.requires_grad == paddle_result.stop_gradient:
            return False
        if str(pytorch_result.dtype)[6:] != str(paddle_result.dtype)[7:]:
            return False
        return True

obj = EmptyAPI('torch.empty')

def test_case_1():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.empty(3)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_2():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.empty(3, 5)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_3():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.empty((4, 4))
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_4():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        shape = [4, 4]
        result = torch.empty(*shape)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_5():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.empty([6, 6], dtype=torch.int64)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_6():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        result = torch.empty([6, 6], dtype=torch.float64, requires_grad=True)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_7():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        flag = True
        result = torch.empty(6, 6, dtype=torch.float64, requires_grad=flag, memory_format=torch.contiguous_format)
        '''
    )
    obj.run(pytorch_code, ['result'])

def test_case_8():
    pytorch_code = textwrap.dedent(
        '''
        import torch
        a = 3
        out = torch.tensor([2., 3.], dtype=torch.float64)
        result = torch.empty(a, a, out=out, dtype=torch.float64, requires_grad=True)
        '''
    )
    obj.run(pytorch_code, ['result', 'out'])



