def torch_cuda_check():
    import torch
    from torch.utils.cpp_extension import CUDA_HOME

    print("CUDA Home:", CUDA_HOME)
    print("torch ver.:", torch.__version__)
    print("Torch CUDA Path:", torch.cuda_path)
    print("CUDA Version:", torch.cuda_version)
    print("CUDA Available:", torch.cuda.is_available())

if __name__ == "__main__":
    torch_cuda_check()