Import("env")


# --- Add custom macros for the ALL files which name contains "http"
def extra_http_configuration(env, node):
    """
    `node.name` - a name of File System Node
    `node.get_path()` - a relative path
    `node.get_abspath()` - an absolute path
    """
    
    # now, we can override ANY SCons variables (CPPDEFINES, CCFLAGS, etc.,) for the specific file
    # pass SCons variables as extra keyword arguments to `env.Object()` function
    # p.s: run `pio run -t envdump` to see a list with SCons variables

    return env.Object(
        node,
        CPPDEFINES=env["CPPDEFINES"],
        CCFLAGS=env["CCFLAGS"] + ["-Wno-stringop-truncation"]
    )

env.AddBuildMiddleware(extra_http_configuration, "*/core_http_client.c")


# --- Replace some file from a build process with another

# def replace_node_with_another(env, node):
#     return env.File("path/to/patched/RtosTimer.cpp")

# env.AddBuildMiddleware(
#     replace_node_with_another,
#     "framework-mbed/rtos/RtosTimer.cpp"
# )


# --- Skip assembly *.S files from build process

# def skip_asm_from_build(env, node):
#     # to ignore file from a build process, just return None
#     return None

# env.AddBuildMiddleware(skip_asm_from_build, "*.S")